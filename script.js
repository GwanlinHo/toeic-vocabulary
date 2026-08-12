let cachedWords = {
    green: [],
    blue: [],
    gold: []
};
let currentLevel = 'green';
let currentWord = null;
let learnedWords = JSON.parse(localStorage.getItem('toeic_learned_words') || '[]');

// 初始化：讀取上次存儲的等級並載入
async function init() {
    // 讀取上次存儲的等級
    const savedLevel = localStorage.getItem('toeic_level') || 'green';
    await setLevel(savedLevel);
}

// 更新進度顯示
function updateProgressUI() {
    const words = cachedWords[currentLevel];
    if (!words || words.length === 0) return;

    // 計算目前等級中，有多少字已經被標記為已學會
    const currentLearnedCount = words.filter(w => learnedWords.includes(w.word)).length;
    const remainingCount = words.length - currentLearnedCount;

    document.getElementById('progress-text').innerText = `剩餘：${remainingCount} / ${words.length} 字`;
}

// 設定等級並動態下載單字
async function setLevel(level) {
    stopImmersive();
    currentLevel = level;
    localStorage.setItem('toeic_level', level);

    // 更新 UI 狀態
    document.body.className = `theme-${level}`;
    document.querySelectorAll('.level-selector button').forEach(btn => btn.classList.remove('active'));
    const activeBtn = document.getElementById(`btn-${level}`);
    if (activeBtn) activeBtn.classList.add('active');

    // 檢查是否有快取，若無則下載
    if (cachedWords[level].length === 0) {
        try {
            const response = await fetch(`data_${level}.json`);
            if (!response.ok) throw new Error(`無法載入 data_${level}.json`);
            cachedWords[level] = await response.json();
        } catch (error) {
            console.error("載入單字庫失敗:", error);
            document.getElementById('meaning').innerText = `資料載入失敗: ${level} 等級單字庫。`;
            return;
        }
    }

    updateProgressUI();
    advanceWord();
}

// 隨機抽取並顯示下一個單字（內部用，不影響沉浸模式）
// 回傳 true 表示成功顯示一個有效單字；false 表示無資料或已全部學完
function advanceWord() {
    const allWords = cachedWords[currentLevel];
    if (!allWords || allWords.length === 0) {
        document.getElementById('word').innerText = "無資料";
        return false;
    }

    // 過濾掉已學會的單字
    const availableWords = allWords.filter(w => !learnedWords.includes(w.word));

    if (availableWords.length === 0) {
        document.getElementById('word').innerText = "恭喜完成！";
        document.getElementById('meaning').innerText = "此等級所有單字已學完。";
        document.getElementById('phonetic').innerText = "";
        document.getElementById('pos').innerText = "Done";
        return false;
    }

    // 隨機抽取（確保不與上一個重複）
    let randomIndex;
    if (availableWords.length > 1) {
        do {
            randomIndex = Math.floor(Math.random() * availableWords.length);
        } while (availableWords[randomIndex] === currentWord);
    } else {
        randomIndex = 0;
    }

    currentWord = availableWords[randomIndex];
    displayWord(currentWord);
    return true;
}

// 使用者手動點「下一個單字」：會先停止沉浸模式
function nextWord() {
    stopImmersive();
    advanceWord();
}

// 標記目前單字為已學會
function markAsLearned() {
    stopImmersive();
    if (!currentWord) return;

    const confirmMark = confirm(`確定要將「${currentWord.word}」標記為已學會並排除嗎？\n(此動作下次不會再出現該字)`);

    if (confirmMark) {
        if (!learnedWords.includes(currentWord.word)) {
            learnedWords.push(currentWord.word);
            localStorage.setItem('toeic_learned_words', JSON.stringify(learnedWords));
            updateProgressUI();
            advanceWord(); // 自動跳轉到下一個
        }
    }
}

// 重設進度
function resetProgress() {
    stopImmersive();
    const words = cachedWords[currentLevel];
    const confirmReset = confirm(`確定要重設「${currentLevel}」等級的學習進度嗎？\n這將會讓所有已標記的單字重新出現。`);

    if (confirmReset) {
        // 僅移除目前等級相關的已學會單字（或是全部移除，此處選擇全部移除較簡單直觀）
        learnedWords = [];
        localStorage.removeItem('toeic_learned_words');
        updateProgressUI();
        advanceWord();
        alert("進度已重設。");
    }
}

// 顯示單字到網頁
function displayWord(data) {
    document.getElementById('word').innerText = data.word || '-';
    document.getElementById('phonetic').innerText = data.phonetic || '';
    document.getElementById('pos').innerText = posToChineseList(data.pos).join('／') || '';
    document.getElementById('meaning').innerText = data.meaning || '無解釋';

    // 處理同義詞與反義詞
    document.getElementById('synonyms').innerText = (data.synonyms && data.synonyms.length > 0) ? data.synonyms.join(', ') : '-';
    document.getElementById('antonyms').innerText = (data.antonyms && data.antonyms.length > 0) ? data.antonyms.join(', ') : '-';
    document.getElementById('example').innerText = data.example || '';
    document.getElementById('example-zh').innerText = data.example_zh || '';

    // 處理片語清單
    const phrasesEl = document.getElementById('phrases');
    phrasesEl.innerHTML = '';
    if (data.phrases && data.phrases.length > 0) {
        data.phrases.forEach(p => {
            const li = document.createElement('li');
            li.innerText = p;
            phrasesEl.appendChild(li);
        });
    }
}

let voices = [];

// 初始化語音引擎
function loadVoices() {
    voices = window.speechSynthesis.getVoices();
}

// 監聽語音包載入
window.speechSynthesis.onvoiceschanged = loadVoices;
loadVoices();

/**
 * 智慧型語音選擇器
 * 優先尋找各系統的高品質自然音 (iOS: Samantha/Siri, Android: Google)
 * 優先選用台灣腔調 (zh-TW) 語音包
 */
function getBestVoice(isChinese) {
    // 優先順序關鍵字
    const enKeywords = ['Samantha (Enhanced)', 'Samantha', 'Google US English', 'Alex', 'Siri', 'Google', 'Microsoft Zira'];
    // 優先權給予 Siri 與 Google 台灣
    const zhKeywords = ['Siri', 'Google 國語（台灣）', 'Google', 'Microsoft Hanhan'];

    const keywords = isChinese ? zhKeywords : enKeywords;

    // 1. 嘗試匹配高品質關鍵字且語系正確
    for (const keyword of keywords) {
        const voice = voices.find(v => {
            const name = v.name;
            const lang = v.lang.toLowerCase().replace('_', '-');
            const isTW = lang.includes('tw'); // 嚴格鎖定 TW
            const isEN = lang.startsWith('en');

            if (isChinese) {
                // 確保語系符合繁體中文 (zh-TW)，並嚴格排除中國大陸 (cn) 與香港 (hk)
                const isOtherRegion = lang.includes('cn') || lang.includes('hk') ||
                                     name.includes('China') || name.includes('Mainland') ||
                                     name.includes('Hong Kong') || name.includes('Cantonese');
                if (!isTW || isOtherRegion) return false;

                // 針對 Siri 的特殊處理：優先尋找「聲音 2」或「Voice 2」
                if (keyword === 'Siri') {
                    return name.includes('Siri') && (name.includes('2') || name.includes('Voice 2') || name.includes('聲音 2'));
                }

                return name.includes(keyword);
            } else {
                return name.includes(keyword) && isEN;
            }
        });
        if (voice) return voice;
    }

    // 2. 二次嘗試：若找不到高品質，則找任何符合語系的台灣語音（排除香港粵語）
    if (isChinese) {
        const anyTW = voices.find(v => {
            const l = v.lang.toLowerCase().replace('_', '-');
            return l.includes('tw') && !l.includes('hk');
        });
        if (anyTW) return anyTW;
    }

    // 3. 最終回退方案
    return voices.find(v => {
        const l = v.lang.toLowerCase().replace('_', '-');
        return isChinese ? (l.includes('tw') && !l.includes('hk')) : l.startsWith('en-us');
    }) || voices.find(v => v.lang.toLowerCase().startsWith(isChinese ? 'zh-tw' : 'en-us'));
}

// 朗讀前清掉會被 TTS 唸出來的標點（Android 會把逗號/句號唸成「comma/dot」，
// iOS 本就略過）。換成空白以保留詞界；刻意保留撇號(don't 不變 dont)與
// $ % & @ 等有意義符號。全形/半形標點與 CJK 括號一併處理。
const SPEECH_PUNCT_RE = /[.,;:!?…"“”„‚«»()\[\]{}\-–—、。，；：！？、「」『』（）〈〉《》【】〔〕～]/g;
function stripSpeechPunctuation(text) {
    return String(text).replace(SPEECH_PUNCT_RE, ' ').replace(/\s+/g, ' ').trim();
}

// 將文字依中文字元與非中文字元（英文、符號）切分成語段（切分前先清標點）
function splitSegments(text) {
    if (!text) return [];
    const clean = stripSpeechPunctuation(text);
    if (!clean) return [];
    return (clean.match(/[一-龥]+|[^一-龥]+/g) || [])
        .map(s => s.trim())
        .filter(Boolean);
}

// 英文開頭墊音：原本用標點停頓試圖蓋住切音，但 iOS 會把句點唸成「dot」、
// 逗號也無助於切音；改由 Web Audio 無聲保活負責防切音，這裡不再加任何前綴。
const EN_LEAD_IN = '';

// 依語言建立一段語音（自動選最佳語音包與語速）
function buildUtterance(text) {
    const isChinese = /[一-龥]/.test(text);
    // 英文段前墊短停頓；中文不受此問題影響，維持原樣
    const spoken = isChinese ? text : EN_LEAD_IN + text;
    const msg = new SpeechSynthesisUtterance(spoken);

    const bestVoice = getBestVoice(isChinese);
    if (bestVoice) {
        msg.voice = bestVoice;
        msg.lang = bestVoice.lang;
    } else {
        msg.lang = isChinese ? 'zh-TW' : 'en-US';
    }

    msg.volume = 1;
    // 英文 0.72 (更利於辨識細節)，中文 0.8
    msg.rate = isChinese ? 0.8 : 0.72;
    msg.pitch = 1;
    return msg;
}

// 核心朗讀邏輯：單次、射後不理（供單鍵朗讀使用）
function speakText(text) {
    splitSegments(text).forEach(seg => {
        window.speechSynthesis.speak(buildUtterance(seg));
    });
}

// 例句前的停頓（讓片語與例句之間有明顯間隔）
const SECTION_PAUSE_MS = 2000;

// 每張卡開頭主詞重複朗讀次數與間隔（加深印象）
const WORD_REPEAT = 3;
const WORD_REPEAT_GAP_MS = 1000;

// 詞性英文縮寫 → 中文對照（涵蓋資料中所有出現過的 token）
const POS_ZH = {
    'n.': '名詞', 'v.': '動詞', 'adj.': '形容詞', 'adv.': '副詞',
    'prep.': '介系詞', 'conj.': '連接詞', 'pron.': '代名詞', 'int.': '感嘆詞',
    'phr.': '片語', 'phrase': '片語', 'idiom': '慣用語',
    'n. phrase': '名詞片語', 'n. phr.': '名詞片語',
    'v. phr.': '動詞片語', 'v. phrase': '動詞片語',
    'adj. phrase': '形容詞片語', 'adj. phr.': '形容詞片語',
    'adv. phr.': '副詞片語',
    'prep. phr.': '介系詞片語', 'prep. phrase': '介系詞片語',
    'conj. phr.': '連接詞片語',
    'n. pl.': '名詞（複數）',
    'v. (past)': '動詞（過去式）', 'v. phr. (past)': '動詞片語（過去式）',
    'adj. (comparative)': '形容詞（比較級）',
    'modal v.': '情態動詞'
};

// 把 pos 依「/」拆開並各自翻成中文；找不到對照則保留原字串
function posToChineseList(rawPos) {
    if (!rawPos) return [];
    return rawPos.split('/')
        .map(p => p.trim())
        .filter(Boolean)
        .map(t => POS_ZH[t] || t);
}

// 組出整張卡片要朗讀的文字清單
// 順序：單字、詞性、解釋、片語、同義詞、反義詞、[停頓]、例句
// 陣列元素可為字串（朗讀）或 { pause: 毫秒 }（靜音停頓）
function cardTexts(w) {
    if (!w) return [];
    // 主詞重複 WORD_REPEAT 遍，每遍間隔 WORD_REPEAT_GAP_MS（加深印象）
    const arr = [];
    for (let r = 0; r < WORD_REPEAT; r++) {
        arr.push(w.word);
        if (r < WORD_REPEAT - 1) arr.push({ pause: WORD_REPEAT_GAP_MS });
    }
    // 詞性翻成中文並拆開分別唸（如 n./v. → 名詞、動詞）
    posToChineseList(w.pos).forEach(p => arr.push(p));
    if (w.meaning) arr.push(w.meaning);
    if (w.phrases && w.phrases.length > 0) w.phrases.forEach(p => arr.push(p));
    if (w.synonyms && w.synonyms.length > 0) {
        arr.push('同義詞');
        arr.push(w.synonyms.join(', '));
    }
    if (w.antonyms && w.antonyms.length > 0) {
        arr.push('反義詞');
        arr.push(w.antonyms.join(', '));
    }
    if (w.example) {
        arr.push({ pause: SECTION_PAUSE_MS }); // 同/反義詞與例句之間停頓
        arr.push(w.example);
        if (w.example_zh) arr.push(w.example_zh); // 例句中文翻譯（英文例句後接著唸）
    }
    return arr;
}

// 播放世代：每次取消/重新開始朗讀就 +1，使進行中的接力（含停頓）失效而中斷
let speechEpoch = 0;
function cancelSpeech() {
    speechEpoch++;
    window.speechSynthesis.cancel();
    stopAudioKeepAlive();
}

/* ===== iOS 切音改善：Web Audio 音訊保活 + 輕提示音 =====
 * iOS Safari 的喇叭音訊通道在每段語音起始前是關著的，喚醒延遲會吃掉第一個音節。
 * 對策：播放期間讓 Web Audio 持續輸出「聽不到的極低訊號」把通道撐開（保活），
 * 並在每張卡開頭放一個很短的柔和提示音，確保通道確實被開啟。
 * AudioContext 必須在使用者手勢中建立/resume。
 */
let audioCtx = null;
let keepAliveNode = null;

function ensureAudioCtx() {
    try {
        if (!audioCtx) {
            const AC = window.AudioContext || window.webkitAudioContext;
            if (!AC) return null;
            audioCtx = new AC();
        }
        if (audioCtx.state === 'suspended') audioCtx.resume();
        return audioCtx;
    } catch (e) {
        return null;
    }
}

// 無聲保活：極低頻、極小音量，聽不到但維持音訊通道開啟
function startAudioKeepAlive() {
    const ctx = ensureAudioCtx();
    if (!ctx || keepAliveNode) return;
    try {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        gain.gain.value = 0.0001; // 約 -80dB，實質無聲
        osc.frequency.value = 20; // 極低頻，聽不太到
        osc.connect(gain).connect(ctx.destination);
        osc.start();
        keepAliveNode = { osc: osc, gain: gain };
    } catch (e) { /* 忽略 */ }
}

function stopAudioKeepAlive() {
    try {
        if (keepAliveNode) {
            keepAliveNode.osc.stop();
            keepAliveNode.osc.disconnect();
            keepAliveNode = null;
        }
        if (audioCtx && audioCtx.state === 'running') audioCtx.suspend();
    } catch (e) { /* 忽略 */ }
}

// 每張卡/播放開頭：確保音訊通道仍開著（無聲，不發提示音）
function playCue() {
    ensureAudioCtx();      // 已建立的 context 若被暫停則 resume
    startAudioKeepAlive(); // 保活若因故停止則重新撐開通道
}

// 循序朗讀一串項目，全部完成後呼叫 onDone（供沉浸模式接力）
// items 元素可為字串（朗讀）或 { pause: 毫秒 }（靜音停頓）
function speakSequence(items, onDone) {
    const queue = [];
    items.forEach(it => {
        if (it && typeof it === 'object' && it.pause) {
            queue.push({ pause: it.pause });
        } else {
            splitSegments(it).forEach(s => queue.push({ say: s }));
        }
    });
    if (queue.length === 0) {
        if (onDone) onDone();
        return;
    }

    const myEpoch = speechEpoch;
    let i = 0;
    function playNext() {
        if (myEpoch !== speechEpoch) return; // 已被取消/換新一輪，中斷
        if (i >= queue.length) {
            if (onDone) onDone();
            return;
        }
        const item = queue[i];
        i++;
        if (item.pause) {
            setTimeout(playNext, item.pause); // 靜音停頓
            return;
        }
        const msg = buildUtterance(item.say);
        msg.onend = playNext;
        msg.onerror = playNext; // 遇錯也繼續，避免卡住
        window.speechSynthesis.speak(msg);
    }
    playNext();
}

// 語音朗讀單字
function speak() {
    if (!currentWord) return;
    cancelSpeech();
    startAudioKeepAlive();
    playCue();
    speakSequence([currentWord.word], stopAudioKeepAlive);
}

// 語音朗讀全卡片內容
function speakAll() {
    if (!currentWord) return;
    cancelSpeech();
    startAudioKeepAlive();
    playCue();
    speakSequence(cardTexts(currentWord), stopAudioKeepAlive);
}

/* ===== 沉浸式連續朗讀模式 ===== */
const IMMERSIVE_HOUR_MS = 60 * 60 * 1000; // 最長持續 1 小時
const IMMERSIVE_REPEAT = 3;               // 每張朗讀 3 次
const IMMERSIVE_GAP_MS = 3000;            // 同張三次之間間隔 3 秒
const IMMERSIVE_SWITCH_MS = 3000;         // 換卡後等待 3 秒才開始朗讀

const immersive = {
    active: false,
    repeatLeft: 0,
    startTime: 0,
    wakeLock: null,
    keepAlive: null,
    timers: [],
    pendingResume: false   // 背景暫停後、回前景需自動接續的旗標
};

// 排入可被統一清除的計時器
function scheduleTimer(fn, ms) {
    const id = setTimeout(() => {
        immersive.timers = immersive.timers.filter(t => t !== id);
        fn();
    }, ms);
    immersive.timers.push(id);
}

function clearImmersiveTimers() {
    immersive.timers.forEach(clearTimeout);
    immersive.timers = [];
}

// 播放期間維持螢幕恆亮（不支援的瀏覽器自動退回一般行為）
async function requestWakeLock() {
    try {
        if ('wakeLock' in navigator) {
            immersive.wakeLock = await navigator.wakeLock.request('screen');
        }
    } catch (e) {
        // 不支援或被拒絕時忽略
    }
}

function releaseWakeLock() {
    try {
        if (immersive.wakeLock) {
            immersive.wakeLock.release();
            immersive.wakeLock = null;
        }
    } catch (e) { /* 忽略 */ }
}

function updateImmersiveButton() {
    const btn = document.getElementById('immersive-btn');
    if (!btn) return;
    if (immersive.active) {
        btn.innerText = '停止沉浸朗讀';
        btn.classList.add('active');
    } else {
        btn.innerText = '開始沉浸朗讀';
        btn.classList.remove('active');
    }
}

function toggleImmersive() {
    if (immersive.active) {
        stopImmersive();
    } else {
        startImmersive();
    }
}

function startImmersive() {
    const allWords = cachedWords[currentLevel] || [];
    const available = allWords.filter(w => !learnedWords.includes(w.word));
    if (available.length === 0) {
        alert('此等級已無可朗讀的單字。');
        return;
    }
    // 若目前不是有效單字（例如已學會或完成畫面），先抽一張
    if (!currentWord || learnedWords.includes(currentWord.word)) {
        advanceWord();
    }

    immersive.active = true;
    immersive.startTime = Date.now();
    updateImmersiveButton();
    requestWakeLock();

    // 保活：部分瀏覽器語音約 15 秒後會自動停頓，定期 resume
    immersive.keepAlive = setInterval(() => {
        if (immersive.active) window.speechSynthesis.resume();
    }, 10000);

    cancelSpeech();
    startAudioKeepAlive();
    immersivePlayCurrent();
}

function stopImmersive(reason) {
    if (!immersive.active) return;
    immersive.active = false;
    immersive.pendingResume = false;
    clearImmersiveTimers();
    if (immersive.keepAlive) {
        clearInterval(immersive.keepAlive);
        immersive.keepAlive = null;
    }
    cancelSpeech();
    releaseWakeLock();
    updateImmersiveButton();

    if (reason) {
        const el = document.getElementById('progress-text');
        if (el) {
            el.innerText = reason;
            setTimeout(updateProgressUI, 2500);
        }
    }
}

// 開始朗讀目前這張卡（共 3 次）
function immersivePlayCurrent() {
    playCue(); // 每張卡開頭的輕提示音（同時撐開音訊通道）
    immersive.repeatLeft = IMMERSIVE_REPEAT;
    immersiveReadOnce();
}

function immersiveReadOnce() {
    if (!immersive.active) return;
    if (Date.now() - immersive.startTime >= IMMERSIVE_HOUR_MS) {
        stopImmersive('已達 1 小時，自動停止');
        return;
    }
    speakSequence(cardTexts(currentWord), () => {
        if (!immersive.active) return;
        immersive.repeatLeft--;
        if (immersive.repeatLeft > 0) {
            // 同一張，間隔 3 秒後再讀一次
            scheduleTimer(immersiveReadOnce, IMMERSIVE_GAP_MS);
        } else {
            // 三次讀完，等 5 秒換下一張
            scheduleTimer(immersiveAdvance, IMMERSIVE_SWITCH_MS);
        }
    });
}

function immersiveAdvance() {
    if (!immersive.active) return;
    if (Date.now() - immersive.startTime >= IMMERSIVE_HOUR_MS) {
        stopImmersive('已達 1 小時，自動停止');
        return;
    }
    const shown = advanceWord(); // 隨機下一張，內建跳過已學會
    if (!shown) {
        stopImmersive('此等級已全部學完');
        return;
    }
    immersivePlayCurrent();
}

// 沉浸模式下切換前景/背景：離開時乾淨暫停，回前景時自動從當前這張卡續讀。
// （背景時瀏覽器會暫停語音；不主動中斷會在回前景後卡死不續讀。）
document.addEventListener('visibilitychange', () => {
    if (!immersive.active) return;
    if (document.visibilityState === 'hidden') {
        // 乾淨中斷在飛的朗讀與待觸發計時器，標記待續，active 維持 true
        cancelSpeech();
        clearImmersiveTimers();
        immersive.pendingResume = true;
    } else if (document.visibilityState === 'visible') {
        requestWakeLock(); // 背景時 Wake Lock 會被釋放，回前景重取
        if (immersive.pendingResume) {
            immersive.pendingResume = false;
            cancelSpeech();          // 保險：清掉任何殘留接力
            clearImmersiveTimers();
            immersivePlayCurrent();  // 從目前這張卡重讀（playCue 會 resume 被暫停的音訊通道）
        }
    }
});

// 啟動程式
init();
