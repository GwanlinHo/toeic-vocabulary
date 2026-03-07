let cachedWords = {
    green: [],
    blue: [],
    gold: []
};
let currentLevel = 'green';
let currentWord = null;

// 初始化：讀取上次存儲的等級並載入
async function init() {
    // 讀取上次存儲的等級
    const savedLevel = localStorage.getItem('toeic_level') || 'green';
    await setLevel(savedLevel);
}

// 設定等級並動態下載單字
async function setLevel(level) {
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
    
    nextWord();
}

// 隨機抽取下一個單字
function nextWord() {
    const words = cachedWords[currentLevel];
    if (!words || words.length === 0) {
        document.getElementById('word').innerText = "無資料";
        return;
    }

    // 隨機抽取（確保不與上一個重複，若只有一字則不檢查）
    let randomIndex;
    if (words.length > 1) {
        do {
            randomIndex = Math.floor(Math.random() * words.length);
        } while (words[randomIndex] === currentWord);
    } else {
        randomIndex = 0;
    }

    currentWord = words[randomIndex];
    displayWord(currentWord);
}

// 顯示單字到網頁
function displayWord(data) {
    document.getElementById('word').innerText = data.word || '-';
    document.getElementById('phonetic').innerText = data.phonetic || '';
    document.getElementById('pos').innerText = data.pos || '';
    document.getElementById('meaning').innerText = data.meaning || '無解釋';
    
    // 處理同義詞與反義詞
    document.getElementById('synonyms').innerText = (data.synonyms && data.synonyms.length > 0) ? data.synonyms.join(', ') : '-';
    document.getElementById('antonyms').innerText = (data.antonyms && data.antonyms.length > 0) ? data.antonyms.join(', ') : '-';
    document.getElementById('example').innerText = data.example || '';

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

// 核心朗讀邏輯：支援中英文自動偵測與分段播放
function speakText(text) {
    if (!text) return;

    // 將文字依中文字元與非中文字元（英文、符號）切分
    const segments = text.match(/[\u4e00-\u9fa5]+|[^\u4e00-\u9fa5]+/g) || [];

    segments.forEach(segment => {
        const trimmed = segment.trim();
        if (!trimmed) return;

        const msg = new SpeechSynthesisUtterance(trimmed);
        const isChinese = /[\u4e00-\u9fa5]/.test(trimmed);
        
        if (isChinese) {
            msg.lang = 'zh-TW';
            const zhVoice = voices.find(v => v.lang.includes('zh-TW') || v.lang.includes('zh-HK') || v.lang.includes('zh-CN'));
            if (zhVoice) msg.voice = zhVoice;
        } else {
            msg.lang = 'en-US';
            const enVoice = voices.find(v => v.lang.includes('en-US') || v.lang.includes('en-GB') || v.lang.includes('en-AU'));
            if (enVoice) msg.voice = enVoice;
        }

        msg.volume = 1;
        msg.rate = 0.9; 
        msg.pitch = 1;
        
        // 瀏覽器會自動排隊播放
        window.speechSynthesis.speak(msg);
    });
}

// 語音朗讀單字
function speak() {
    if (!currentWord) return;
    window.speechSynthesis.cancel();
    speakText(currentWord.word);
}

// 語音朗讀全卡片內容
function speakAll() {
    if (!currentWord) return;
    
    // 先停止當前所有朗讀
    window.speechSynthesis.cancel();

    // 依序加入播放隊列
    // 1. 單字與詞性
    speakText(currentWord.word);
    if (currentWord.pos) speakText(currentWord.pos);
    
    // 2. 中文解釋
    speakText(currentWord.meaning);

    // 3. 片語
    if (currentWord.phrases && currentWord.phrases.length > 0) {
        currentWord.phrases.forEach(p => speakText(p));
    }

    // 4. 例句
    if (currentWord.example) speakText(currentWord.example);
}

// 啟動程式
init();
