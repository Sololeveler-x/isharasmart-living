import re

with open('home/site.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

glass_rules = re.findall(r'(\.riva-card-glass[^{]*\{[^}]*\})', css)
print("riva-card-glass rules:", glass_rules)

header_rules = re.findall(r'(#header-bar[^{]*\{[^}]*\})', css)
print("header-bar rules:", header_rules[:5])

# Also check for .riva-device-card
card_rules = re.findall(r'(\.riva-device-card[^{]*\{[^}]*\})', css)
print("riva-device-card rules:", card_rules[:5])
