/* 多益單字：沉浸朗讀的 Wake Lock 行為
 *
 * 用假的語音引擎與假的 Wake Lock 跑真正的頁面，驗證四件事：
 * 被系統收回時會補回、已握著時不重複要、背景不要、停止後不殘留。
 * 執行方式：tests/run_tests.sh（會自己起本機伺服器）。
 * 需要 puppeteer-core，路徑可用環境變數 PUPPETEER_PATH 覆蓋。 */
const puppeteer = require(process.env.PUPPETEER_PATH || "/home/pi/WorkDir/browser-tool/node_modules/puppeteer-core");
const BASE = process.env.BASE || "http://127.0.0.1:8141/index.html";
let fail = 0;
function ok(cond, msg) { console.log((cond ? "[O] " : "[X] ") + msg); if (!cond) fail++; }
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    executablePath: process.env.CHROMIUM_PATH || "/usr/bin/chromium-browser",
    headless: "new",
    args: ["--no-sandbox", "--autoplay-policy=no-user-gesture-required"],
  });
  const page = await browser.newPage();
  page.on("pageerror", (e) => { console.log("[X] page error: " + e.message); fail++; });
  await page.evaluateOnNewDocument(() => {
    window.alert = () => {};
    window.__vis = "visible";
    Object.defineProperty(document, "visibilityState", { configurable: true, get: () => window.__vis });
    const synth = {
      speaking: false, paused: false, pending: false,
      getVoices: () => [],
      speak(u) { setTimeout(() => { if (u.onend) u.onend({}); }, 20); },
      cancel() {}, pause() {}, resume() {},
      addEventListener() {}, onvoiceschanged: null,
    };
    Object.defineProperty(window, "speechSynthesis", { configurable: true, value: synth });
    Object.defineProperty(window, "SpeechSynthesisUtterance", {
      configurable: true,
      value: function (t) { this.text = t; this.lang = ""; this.rate = 1; this.pitch = 1; this.volume = 1; },
    });
    const w = window.__wake = { requests: 0, releases: 0, locks: [], delay: 0 };
    w.held = () => w.locks.filter((l) => !l.released).length;
    w.systemRelease = () => w.locks.forEach((l) => l.fire());
    Object.defineProperty(navigator, "wakeLock", {
      configurable: true,
      value: {
        request() {
          w.requests++;
          const handlers = [];
          const lock = {
            released: false,
            fire() { if (lock.released) return; lock.released = true; handlers.forEach((h) => h({})); },
            release() { if (!lock.released) w.releases++; lock.fire(); return Promise.resolve(); },
            addEventListener(ev, fn) { if (ev === "release") handlers.push(fn); },
          };
          return new Promise((res) => setTimeout(() => { w.locks.push(lock); res(lock); }, w.delay));
        },
      },
    });
  });
  await page.goto(BASE, { waitUntil: "domcontentloaded" });
  await page.waitForFunction(() => {
    const t = document.getElementById("word").textContent;
    return t && t !== "Loading...";
  }, { timeout: 30000 });

  const W = () => page.evaluate(() => ({
    requests: __wake.requests, releases: __wake.releases, held: __wake.held(),
    has: !!immersive.wakeLock, active: immersive.active,
  }));
  const visibility = (st) => page.evaluate((s) => {
    window.__vis = s;
    document.dispatchEvent(new Event("visibilitychange"));
  }, st);

  // 1. 開始沉浸朗讀取得一把鎖
  await page.click("#immersive-btn");
  await page.waitForFunction(() => __wake.held() === 1 && !!immersive.wakeLock, { timeout: 5000 });
  let s = await W();
  ok(s.requests === 1 && s.held === 1, "開始沉浸朗讀取得一把 Wake Lock " + JSON.stringify(s));

  // 2. 沒切背景卻收到回前景事件：不重複要
  await visibility("visible");
  await sleep(300);
  s = await W();
  ok(s.requests === 1 && s.held === 1, "已握著鎖時回前景事件不重複要求 " + JSON.stringify(s));

  // 3. 畫面上被系統收回：10 秒定期檢查補回
  await page.evaluate(() => __wake.systemRelease());
  s = await W();
  ok(s.held === 0 && !s.has, "系統收回後狀態清掉 " + JSON.stringify(s));
  await page.waitForFunction(() => __wake.held() === 1, { timeout: 12000 }).catch(() => {});
  s = await W();
  ok(s.requests === 2 && s.held === 1 && s.has, "沒離開畫面，定期檢查在 10 秒內補回 " + JSON.stringify(s));

  // 4. 切背景（系統收回）→ 背景時不要 → 回前景補回
  await visibility("hidden");
  await page.evaluate(() => __wake.systemRelease());
  await sleep(300);
  s = await W();
  ok(s.requests === 2 && s.held === 0, "背景時不去要 Wake Lock " + JSON.stringify(s));
  await visibility("visible");
  await page.waitForFunction(() => __wake.held() === 1, { timeout: 5000 }).catch(() => {});
  s = await W();
  ok(s.requests === 3 && s.held === 1 && s.active, "回前景補回一把並繼續沉浸朗讀 " + JSON.stringify(s));

  // 5. 停止後放掉
  await page.click("#immersive-btn");
  await sleep(200);
  s = await W();
  ok(!s.active && s.held === 0 && !s.has, "停止沉浸朗讀後放掉 Wake Lock " + JSON.stringify(s));

  // 6. 取得還沒回來就停止：之後回來的鎖要立刻放掉
  await page.evaluate(() => { __wake.delay = 600; });
  await page.click("#immersive-btn");
  await sleep(100);
  await page.click("#immersive-btn");
  await sleep(900);
  s = await W();
  ok(!s.active && s.held === 0 && !s.has, "取得途中停止，之後拿到的鎖立刻放掉 " + JSON.stringify(s));

  await browser.close();
  console.log(fail === 0 ? "ALL PASSED" : "FAILED " + fail);
  process.exit(fail ? 1 : 0);
})().catch((e) => { console.log("[X] " + e.stack); process.exit(1); });
