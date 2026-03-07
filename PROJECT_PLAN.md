# 多益單字隨身卡 (TOEIC Flashcard Web) 實作計畫書

本專案旨在建立一個輕量、反應快速的靜態網頁，幫助使用者利用碎片時間複習多益高頻單字。透過 GitHub Pages 部署，並可完美整合至 iOS 捷徑中。

## 1. 專案目標
- 提供一個簡潔的介面，每次打開即顯示一個隨機單字。
- 支援根據多益證書等級（綠色、藍色、金色）篩選單字庫。
- 完整呈現單字拼寫、音標、詞性、中文解釋、片語、同反義詞及例句。

## 2. 技術架構
- **前端繪製**：純 HTML5 + CSS3 (採用 Flexbox/Grid 佈局，確保手機端體驗)。
- **邏輯控制**：原生 JavaScript (Vanilla JS)，負責 JSON 資料讀取、隨機演算法及 DOM 更新。
- **資料儲存**：`data.json` 靜態檔案，便於日後擴充單字量。
- **部署環境**：GitHub Pages (HTTPS 存取)。

## 3. 目錄結構
```text
toeic-vocabulary/
├── index.html          # 網頁主體
├── style.css           # 視覺樣式 (響應式設計)
├── script.js           # 抽詞與互動邏輯
├── data.json           # 單字資料庫 (按等級分類)
└── PROJECT_PLAN.md     # 本計畫書
```

## 4. 資料規格 (JSON Schema)
每個單字物件包含以下欄位：
- `word`: 拼寫
- `phonetic`: 音標 (IPA)
- `pos`: 詞性 (n., v., adj., adv.)
- `meaning`: 中文解釋
- `level`: 證書顏色 (green, blue, gold)
- `phrases`: 片語或搭配詞 (Array)
- `synonyms`: 同義詞 (Array)
- `antonyms`: 反義詞 (Array)
- `example`: 例句 (包含翻譯)

## 5. UI/UX 設計重點
- **配色方案**：預設背景為深色或暖白色，按選取的證書等級動態切換強調色（綠/藍/金）。
- **單字卡片**：置中顯示，大字體標題，下方為詳細資訊摺疊區或滾動區。
- **操作按鈕**：
    - 等級切換按鈕。
    - 「下一個」隨機按鈕。
    - 「語音朗讀」 (利用 Web Speech API)。

## 6. 部署流程
1. 將專案推送到 GitHub Repository。
2. 進入 Repository 設定 (Settings) -> Pages。
3. 選擇 `main` 分支並儲存。
4. 取得 GitHub 提供的 URL。

## 7. iOS 捷徑整合建議
1. 打開 iOS 「捷徑」App，新增捷徑。
2. 加入「URL」動作，貼入 GitHub Pages 網址。
3. 加入「顯示網頁」動作，選擇上方的 URL。
4. 將捷徑加入主畫面或設為自動化觸發。

---
*註：本文件產出於 2026年3月7日*
