#!/bin/bash

# 多益單字隨身卡 - 本地開發伺服器啟動腳本
PORT=8000

echo "---------------------------------------"
echo "  多益單字隨身卡 (TOEIC Flashcard)     "
echo "  正在啟動本地伺服器...                "
echo "  網址: http://localhost:$PORT         "
echo "---------------------------------------"
echo "提示: 按下 Ctrl + C 可停止伺服器"

# 啟動 Python 內建伺服器
python3 -m http.server $PORT
