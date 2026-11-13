import re

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Check where header-bar is placed
header_idx = html.find('id="header-bar"')
print("header-bar found at index:", header_idx)

# Check ancestors before header-bar
before = html[:header_idx]
tags = re.findall(r'<([a-zA-Z0-9]+)[^>]*>', before)
print("Tags before header-bar:", tags[-10:])

# Check sections IDs
sections = re.findall(r'<section[^>]*>', html)
for s in sections:
    print("Section tag:", s[:80])
