import urllib.request

urls = [
    'http://localhost:8765/home/',
    'http://localhost:8765/home/site.css',
    'http://localhost:8765/home/img/matter.webp',
    'http://localhost:8765/home/img/Smart-Home-%E2%80%93-Day-Curtains-Open-Lights-On-1024x683.webp',
    'http://localhost:8765/tour/index.html'
]

for u in urls:
    try:
        resp = urllib.request.urlopen(u)
        print(f"{resp.status} OK: {u} ({len(resp.read())} bytes)")
    except Exception as e:
        print(f"FAIL: {u} -> {e}")
