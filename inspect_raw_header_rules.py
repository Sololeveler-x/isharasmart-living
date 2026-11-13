import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# Let's search for sticky rules in CSS
print("Searching for sticky / header rules in raw/home.html:")

patterns = [
    r'[^{}]*#header-bar[^{]*\{[^}]*\}',
    r'[^{}]*header-internal[^{]*\{[^}]*\}',
    r'[^{}]*elementor-sticky[^{]*\{[^}]*\}',
    r'[^{}]*elementor-location-header[^{]*\{[^}]*\}',
    r'[^{}]*elementor-element-17c5ac4[^{]*\{[^}]*\}',
    r'[^{}]*elementor-element-127d543[^{]*\{[^}]*\}',
]

for pat in patterns:
    matches = re.findall(pat, raw, re.IGNORECASE)
    print(f"\nPattern: {pat} -> {len(matches)} matches")
    for m in matches[:6]:
        print("  ", m.strip()[:180])
