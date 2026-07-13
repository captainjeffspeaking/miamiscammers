// Self-destruct: wipe all caches, force reload all open tabs, then unregister.
// After this runs once, there is no service worker. Site loads fresh from Netlify every time.
self.addEventListener('install', () => self.skipWaiting());

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.map(k => caches.delete(k))))
      .then(() => self.clients.matchAll({ type: 'window', includeUncontrolled: true }))
      .then(clients => {
        clients.forEach(c => {
          try { c.navigate(c.url); } catch(_) { c.postMessage({ type: 'RELOAD' }); }
        });
      })
      .then(() => self.registration.unregister())
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(fetch(e.request));
});
