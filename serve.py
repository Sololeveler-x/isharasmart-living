# Local server that never lets the browser cache, so every edit shows on reload.
# Run: python3 serve.py   →  http://localhost:8765
import functools, http.server, os

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        if self.path.split('?')[0].endswith(('/', '.html')):
            self.send_header('Clear-Site-Data', '"cache"')   # evict copies cached before this server existed
        super().end_headers()

http.server.ThreadingHTTPServer(('127.0.0.1', 8765), functools.partial(NoCache, directory=os.path.dirname(os.path.abspath(__file__)))).serve_forever()
