#!/bin/bash
# 測試：沉浸朗讀的 Wake Lock 行為（假語音、假 Wake Lock）
# 需求：python3、node、chromium、puppeteer-core
set -u
cd "$(dirname "$0")"

PORT=${PORT:-8141}
STARTED_SERVER=0
if ! curl -s -m 2 -o /dev/null "http://127.0.0.1:$PORT/"; then
  python3 -m http.server "$PORT" --bind 127.0.0.1 --directory .. >/dev/null 2>&1 &
  SERVER_PID=$!
  STARTED_SERVER=1
  sleep 1
fi

FAIL=0
echo "===== 沉浸朗讀螢幕常亮 ====="
BASE="http://127.0.0.1:$PORT/index.html" node wake_e2e.js || FAIL=1

if [ "$STARTED_SERVER" = "1" ]; then
  kill "$SERVER_PID" 2>/dev/null
fi

if [ "$FAIL" = "0" ]; then
  echo "[O] ALL TEST SUITES PASSED"
else
  echo "[X] SOME TESTS FAILED"
fi
exit $FAIL
