import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

print("File size:", len(raw))

# Find header tags
headers = list(re.finditer(r'<header[^>]*>', raw, re.IGNORECASE))
print("Header tags found:", len(headers))
for h in headers:
    pos = h.start()
    print("Header tag:", raw[pos:pos+300])

# Find occurrences of header-bar
for m in re.finditer(r'header-bar', raw):
    pos = m.start()
    print("header-bar occurrence at", pos, ":")
    print(raw[max(0, pos-100):min(len(raw), pos+200)])
    print("="*40)
