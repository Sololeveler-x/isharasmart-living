import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

cta_match = re.search(r'<section[^>]*riva-cta-section[^>]*>.*?</section>', html, re.DOTALL)
if cta_match:
    print("Found CTA section (len=", len(cta_match.group(0)), ")")
    print(cta_match.group(0)[:1500])
else:
    print("CTA section not found")
