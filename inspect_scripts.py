import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

scripts = re.findall(r'<script([^>]*)>(.*?)</script>', html, re.DOTALL)
print(f"Total script tags: {len(scripts)}")

for i, (attrs, body) in enumerate(scripts):
    src_match = re.search(r'src="([^"]*)"', attrs)
    id_match = re.search(r'id="([^"]*)"', attrs)
    id_val = id_match.group(1) if id_match else None
    
    if src_match:
        src = src_match.group(1)
        if src.startswith('data:'):
            print(f"[{i+1}] DATA SCRIPT (id={id_val}) len={len(src)}")
        else:
            print(f"[{i+1}] EXTERNAL SCRIPT: {src}")
    else:
        snippet = body.strip().replace('\n', ' ')[:70]
        print(f"[{i+1}] INLINE SCRIPT (id={id_val}) len={len(body)}: {snippet}")
