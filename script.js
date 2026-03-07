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

// 語音朗讀
function speak() {
    if (!currentWord) return;

    window.speechSynthesis.cancel();
    const msg = new SpeechSynthesisUtterance();
    msg.text = currentWord.word;
    
    const englishVoice = voices.find(v => v.lang.includes('en-US') || v.lang.includes('en-GB'));
    if (englishVoice) msg.voice = englishVoice;

    msg.lang = 'en-US';
    msg.volume = 1;
    msg.rate = 0.9; 
    msg.pitch = 1;

    window.speechSynthesis.speak(msg);
}

// 啟動程式
init();
