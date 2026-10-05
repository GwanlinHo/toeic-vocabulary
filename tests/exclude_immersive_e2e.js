/* 多益單字：沉浸朗讀中按下「排除」或「下一個單字」都不應中斷朗讀
 *
 * 用假的語音引擎與假的 Wake Lock 跑真正的頁面，驗證：
 * 確認排除後沉浸仍在、換了下一張並重新開始朗讀；取消則從當前這張卡重讀；
 * 沉浸中按「下一個單字」當作跳過這張，換字並續讀；
 * 非沉浸狀態下按排除／下一個單字行為不變（不會啟動朗讀）。
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
    // confirm 由測試切換回傳值，並記錄被問過幾次
    window.__confirm = { answer: true, calls: 0 };
    window.confirm = () => { window.__confirm.calls++; return window.__confirm.answer; };
    window.__vis = "visible";
    Object.defineProperty(document, "visibilityState", { configurable: true, get: () => window.__vis });
    // 假語音：記錄每段被唸的文字，20ms 後回報唸完
    window.__spoken = [];
    const synth = {
      speaking: false, paused: false, pending: false,
      getVoices: () => [],
      speak(u) { window.__spoken.push(u.text); setTimeout(() => { if (u.onend) u.onend({}); }, 20); },
      cancel() {}, pause() {}, resume() {},
      addEventListener() {}, onvoiceschanged: null,
    };
    Object.defineProperty(window, "speechSynthesis", { configurable: true, value: synth });
    Object.defineProperty(window, "SpeechSynthesisUtterance", {
      configurable: true,
      value: function (t) { this.text = t; this.lang = ""; this.rate = 1; this.pitch = 1; this.volume = 1; },
    });
    // 假 Wake Lock：只要能成功取得就好
    Object.defineProperty(navigator, "wakeLock", {
      configurable: true,
      value: { request: () => Promise.resolve({ released: false, release: () => Promise.resolve(), addEventListener() {} }) },
    });
  });
  await page.goto(BASE, { waitUntil: "domcontentloaded" });
  await page.waitForFunction(() => {
    const t = document.getElementById("word").textContent;
    return t && t !== "Loading...";
  }, { timeout: 30000 });

  const S = () => page.evaluate(() => ({
    active: immersive.active,
    word: currentWord && currentWord.word,
    learned: learnedWords.length,
    confirms: __confirm.calls,
    spoken: __spoken.length,
  }));
  const setAnswer = (a) => page.evaluate((v) => { window.__confirm.answer = v; }, a);
  const resetSpoken = () => page.evaluate(() => { window.__spoken = []; });

  // 0. 乾淨起點：清掉可能殘留的學習進度
  await page.evaluate(() => {
    learnedWords = [];
    localStorage.removeItem("toeic_learned_words");
    updateProgressUI();
  });

  // 1. 沉浸中按排除並確認：沉浸不中斷、換字、繼續朗讀
  await page.click("#immersive-btn");
  await page.waitForFunction(() => __spoken.length > 0, { timeout: 5000 });
  const before = await S();
  ok(before.active, "沉浸朗讀已啟動 " + JSON.stringify(before));

  await setAnswer(true);
  await resetSpoken();
  await page.click(".learned-btn");
  await sleep(300);
  let s = await S();
  ok(s.confirms === 1, "有跳出確認框 " + JSON.stringify(s));
  ok(s.active, "確認排除後沉浸朗讀仍在進行 " + JSON.stringify(s));
  ok(s.learned === before.learned + 1, "該字已被記為已學會 " + JSON.stringify(s));
  ok(s.word !== before.word, "已換到下一個單字 " + JSON.stringify(s));
  ok(s.spoken > 0, "排除後繼續朗讀新的單字 " + JSON.stringify(s));
  const excluded = before.word;
  ok(await page.evaluate((w) => learnedWords.includes(w), excluded), "被排除的字在 learnedWords 中");

  // 2. 沉浸中按排除但取消：沉浸不中斷、不換字、從當前卡重讀
  const cur = await S();
  await setAnswer(false);
  await resetSpoken();
  await page.click(".learned-btn");
  await sleep(300);
  s = await S();
  ok(s.active, "取消排除後沉浸朗讀仍在進行 " + JSON.stringify(s));
  ok(s.learned === cur.learned, "取消不會寫入已學會 " + JSON.stringify(s));
  ok(s.word === cur.word, "取消後停在同一個單字 " + JSON.stringify(s));
  ok(s.spoken > 0, "取消後從當前這張卡重讀 " + JSON.stringify(s));
  ok(await page.evaluate(() => __spoken[0] === currentWord.word), "重讀是從主詞開始");

  // 3. 沉浸中按「下一個單字」：不中斷、換字、從新卡續讀，且不跳確認框
  const cur2 = await S();
  await resetSpoken();
  await page.click(".next-btn");
  await sleep(300);
  s = await S();
  ok(s.confirms === cur2.confirms, "按下一個單字不會跳確認框 " + JSON.stringify(s));
  ok(s.active, "沉浸中按下一個單字仍在進行朗讀 " + JSON.stringify(s));
  ok(s.word !== cur2.word && s.learned === cur2.learned, "換到下一個單字且不記為已學會 " + JSON.stringify(s));
  ok(s.spoken > 0, "換字後繼續朗讀 " + JSON.stringify(s));

  // 4. 停止沉浸後按排除：維持原行為（換字但不朗讀）
  await page.click("#immersive-btn");
  await sleep(200);
  const off = await S();
  ok(!off.active, "已停止沉浸朗讀 " + JSON.stringify(off));
  await setAnswer(true);
  await resetSpoken();
  await page.click(".learned-btn");
  await sleep(300);
  s = await S();
  ok(!s.active, "非沉浸下按排除不會啟動沉浸 " + JSON.stringify(s));
  ok(s.word !== off.word && s.learned === off.learned + 1, "非沉浸下照舊排除並換字 " + JSON.stringify(s));
  ok(s.spoken === 0, "非沉浸下排除不朗讀 " + JSON.stringify(s));

  // 5. 非沉浸下按「下一個單字」：換字但不朗讀
  const off2 = await S();
  await resetSpoken();
  await page.click(".next-btn");
  await sleep(300);
  s = await S();
  ok(!s.active && s.spoken === 0, "非沉浸下按下一個單字不朗讀 " + JSON.stringify(s));
  ok(s.word !== off2.word && s.learned === off2.learned, "非沉浸下照舊只換字 " + JSON.stringify(s));

  await page.evaluate(() => localStorage.removeItem("toeic_learned_words"));
  await browser.close();
  console.log(fail === 0 ? "ALL PASSED" : "FAILED " + fail);
  process.exit(fail ? 1 : 0);
})().catch((e) => { console.log("[X] " + e.message); process.exit(1); });
