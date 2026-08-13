/* 多益單字隨身卡 Service Worker — 離線快取（cache-first）
   更新方式：改動任何檔案後，把 CACHE 版本號 +1，使用者下次開啟即自動更新。 */
const CACHE = 'toeic-vocab-v1';

// 預先快取的核心資產（相對於 sw.js 所在目錄，故在 project page 子路徑下也正確）
const ASSETS = [
  './',
  './index.html',
  './style.css',
  './script.js',
  './data_green.json',
  './data_blue.json',
  './data_gold.json',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './apple-touch-icon.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((cache) => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req).then((res) => {
        // 執行期取得的同源資源順手快取（例如日後新增檔案）
        if (res && res.status === 200 && req.url.startsWith(self.location.origin)) {
          const copy = res.clone();
          caches.open(CACHE).then((cache) => cache.put(req, copy));
        }
        return res;
      }).catch(() => {
        // 離線且未快取：導覽請求回退到 index.html
        if (req.mode === 'navigate') return caches.match('./index.html');
      });
    })
  );
});
