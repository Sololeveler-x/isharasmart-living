import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

footer_match = re.search(r'<footer[^>]*>.*?</footer>', html, re.DOTALL)
if footer_match:
    print("Found footer (len=", len(footer_match.group(0)), ")")
    print(footer_match.group(0)[:2500])
else:
    print("No <footer> tag found")
