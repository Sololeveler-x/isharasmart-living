import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# Find header CSS in raw/home.html
m = re.findall(r'#header-bar[^{]*\{[^}]*\}', raw)
for rule in m:
    print("RAW rule:", rule)

header_html = re.search(r'<header[^>]*>.*?</header>', raw, re.DOTALL)
if header_html:
    print("Header classes:", re.findall(r'class="([^"]*)"', header_html.group(0))[:10])
