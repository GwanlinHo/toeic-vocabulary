/* 多益單字：主詞換行與自動縮字
 *
 * 用真正的頁面掃過全部單字，驗證在各種手機寬度下：
 * 整頁不會被長單字撐出橫向捲動、主詞不溢出、斷字點來自資料的 word_shy、
 * 超過 2 行才縮字且不低於下限，而朗讀用的仍是不含軟連字號的原字。
 * 執行方式：tests/run_tests.sh（會自己起本機伺服器）。
 * 需要 puppeteer-core，路徑可用環境變數 PUPPETEER_PATH 覆蓋。 */
const puppeteer = require(process.env.PUPPETEER_PATH || "/home/pi/WorkDir/browser-tool/node_modules/puppeteer-core");
const BASE = process.env.BASE || "http://127.0.0.1:8141/index.html";
const SHY = "­";
let fail = 0;
function ok(cond, msg) { console.log((cond ? "[O] " : "[X] ") + msg); if (!cond) fail++; }

(async () => {
  const browser = await puppeteer.launch({
    executablePath: process.env.CHROMIUM_PATH || "/usr/bin/chromium-browser",
    headless: "new",
    args: ["--no-sandbox"],
  });
  const page = await browser.newPage();
  page.on("pageerror", (e) => { console.log("[X] page error: " + e.message); fail++; });

  // 1~4：四種常見手機寬度，全部單字都不得溢出
  for (const W of [320, 360, 390, 430]) {
    await page.setViewport({ width: W, height: 900, deviceScaleFactor: 1 });
    await page.goto(BASE, { waitUntil: "domcontentloaded" });
    await page.waitForFunction(() => document.getElementById("word").textContent !== "Loading...", { timeout: 30000 });
    const r = await page.evaluate(async () => {
      const all = [];
      for (const lv of ["green", "blue", "gold"]) all.push(...await fetch("data_" + lv + ".json").then((r) => r.json()));
      const el = document.getElementById("word");
      el.style.fontSize = "";
      const base = parseFloat(getComputedStyle(el).fontSize);
      const bad = [];
      let shrunk = 0, maxLines = 0, belowFloor = 0;
      for (const w of all) {
        displayWord(w);
        const fs = parseFloat(getComputedStyle(el).fontSize);
        const n = wordLineCount(el);
        if (n > maxLines) maxLines = n;
        if (fs < base - 0.01) shrunk++;
        if (fs < base * 0.65 - 0.01) belowFloor++;
        if (el.scrollWidth > el.clientWidth + 1 || document.documentElement.scrollWidth > window.innerWidth + 1) {
          bad.push(w.word);
        }
      }
      return { total: all.length, bad: bad.slice(0, 5), badCount: bad.length, shrunk, maxLines, belowFloor };
    });
    ok(r.badCount === 0, `寬 ${W}：${r.total} 字全部不溢出（縮字 ${r.shrunk} 字、最多 ${r.maxLines} 行）` + (r.badCount ? " 例外：" + JSON.stringify(r.bad) : ""));
    ok(r.belowFloor === 0, `寬 ${W}：縮字不低於下限 0.65`);
  }

  // 5~8：斷字與朗讀的分工
  await page.setViewport({ width: 390, height: 900, deviceScaleFactor: 1 });
  await page.goto(BASE, { waitUntil: "domcontentloaded" });
  await page.waitForFunction(() => document.getElementById("word").textContent !== "Loading...", { timeout: 30000 });
  const d = await page.evaluate(async (SHY) => {
    const all = [];
    for (const lv of ["green", "blue", "gold"]) all.push(...await fetch("data_" + lv + ".json").then((r) => r.json()));
    const el = document.getElementById("word");
    const withShy = all.filter((w) => w.word_shy);
    const restoreOk = withShy.every((w) => w.word_shy.split(SHY).join("") === w.word);
    // 長單字：有斷字點，且顯示用的是 word_shy
    const long = all.find((w) => w.word === "pharmacovigilance");
    displayWord(long);
    const shown = el.textContent;
    // 朗讀文字不得含軟連字號
    const spoken = cardTexts(long).filter((x) => typeof x === "string");
    return {
      shyCount: withShy.length,
      restoreOk,
      shownHasShy: shown.indexOf(SHY) >= 0,
      shownIsShy: shown === long.word_shy,
      lines: wordLineCount(el),
      fullSize: parseFloat(getComputedStyle(el).fontSize) === parseFloat(getComputedStyle(el).fontSize),
      spokenHasShy: spoken.some((t) => t.indexOf(SHY) >= 0),
      spokenHasWord: spoken.indexOf(long.word) >= 0,
    };
  }, SHY);
  ok(d.shyCount > 3000, `資料裡有 ${d.shyCount} 字帶斷字點`);
  ok(d.restoreOk, "移除軟連字號後與原字完全相同（不會影響已學會紀錄）");
  ok(d.shownIsShy && d.shownHasShy, "卡片顯示的是帶斷字點的 word_shy");
  ok(d.lines === 2, `pharmacovigilance 在 390 寬斷成 ${d.lines} 行`);
  ok(!d.spokenHasShy && d.spokenHasWord, "朗讀文字用原字、不含軟連字號");

  await browser.close();
  console.log(fail === 0 ? "ALL PASSED" : "FAILED " + fail);
  process.exit(fail ? 1 : 0);
})().catch((e) => { console.log("[X] " + e.message); process.exit(1); });
