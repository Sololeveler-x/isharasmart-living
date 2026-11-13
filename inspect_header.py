import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

header_match = re.search(r'<header[^>]*>.*?</header>', html, re.DOTALL)
if header_match:
    print("Found header (len=", len(header_match.group(0)), ")")
    print(header_match.group(0)[:2500])
else:
    print("No <header> tag found, looking for .site-header or sticky header...")
    sticky = re.findall(r'<div[^>]*class="[^"]*(?:header|nav|sticky)[^"]*"[^>]*>', html)
    print("Header divs:", sticky[:10])
