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
    nextWord();
}

// 隨機抽取下一個單字
function nextWord() {
    const allWords = cachedWords[currentLevel];
    if (!allWords || allWords.length === 0) {
        document.getElementById('word').innerText = "無資料";
        return;
    }

    // 過濾掉已學會的單字
    const availableWords = allWords.filter(w => !learnedWords.includes(w.word));

    if (availableWords.length === 0) {
        document.getElementById('word').innerText = "恭喜完成！";
        document.getElementById('meaning').innerText = "此等級所有單字已學完。";
        document.getElementById('phonetic').innerText = "";
        document.getElementById('pos').innerText = "Done";
        return;
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
}

// 標記目前單字為已學會
function markAsLearned() {
    if (!currentWord) return;
    
    const confirmMark = confirm(`確定要將「${currentWord.word}」標記為已學會並排除嗎？\n(此動作下次不會再出現該字)`);
    
    if (confirmMark) {
        if (!learnedWords.includes(currentWord.word)) {
            learnedWords.push(currentWord.word);
            localStorage.setItem('toeic_learned_words', JSON.stringify(learnedWords));
            updateProgressUI();
            nextWord(); // 自動跳轉到下一個
        }
    }
}

// 重設進度
function resetProgress() {
    const words = cachedWords[currentLevel];
    const confirmReset = confirm(`確定要重設「${currentLevel}」等級的學習進度嗎？\n這將會讓所有已標記的單字重新出現。`);
    
    if (confirmReset) {
        // 僅移除目前等級相關的已學會單字（或是全部移除，此處選擇全部移除較簡單直觀）
        learnedWords = [];
        localStorage.removeItem('toeic_learned_words');
        updateProgressUI();
        nextWord();
        alert("進度已重設。");
    }
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
            const isTW = lang.includes('tw') || lang.includes('hant');
            const isEN = lang.startsWith('en');
            
            if (isChinese) {
                // 確保語系符合繁體中文 (zh-TW)
                const isOtherRegion = lang.includes('cn') || name.includes('China') || name.includes('Mainland');
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

    // 2. 二次嘗試：若找不到 Siri 2，則找任何 Siri 或符合語系的台灣語音
    if (isChinese) {
        const anySiri = voices.find(v => v.name.includes('Siri') && (v.lang.includes('tw') || v.lang.includes('hant')));
        if (anySiri) return anySiri;
    }

    // 3. 回退方案：嚴格過濾後的台灣語音
    return voices.find(v => {
        const l = v.lang.toLowerCase().replace('_', '-');
        return isChinese ? (l.includes('tw') || l.includes('hant')) : l.startsWith('en-us');
    }) || voices.find(v => v.lang.toLowerCase().startsWith(isChinese ? 'zh' : 'en'));
}

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
        
        // 取得最佳語音包
        const bestVoice = getBestVoice(isChinese);
        if (bestVoice) {
            msg.voice = bestVoice;
            msg.lang = bestVoice.lang;
        } else {
            msg.lang = isChinese ? 'zh-TW' : 'en-US';
        }

        msg.volume = 1;
        // 進一步調慢語速：英文 0.72 (更利於辨識細節)，中文 0.8
        msg.rate = isChinese ? 0.8 : 0.72; 
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
