import re

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

riva_links = re.findall(r'href="([^"]*rivasmart\.com[^"]*)"', html, re.IGNORECASE)
print(f"Total links pointing to rivasmart.com: {len(riva_links)}")
for l in sorted(list(set(riva_links))):
    print(" -", l)
