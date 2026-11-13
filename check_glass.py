import re

with open('home/site.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

bf = re.findall(r'[^}]*backdrop-filter[^}]*}', css)
print(f"Total rules with backdrop-filter in site.css: {len(bf)}")
for r in bf[:15]:
    print("Rule:", r.strip()[:120])

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

bf_html = re.findall(r'[^}]*backdrop-filter[^}]*}', html)
print(f"Total rules with backdrop-filter in index.html: {len(bf_html)}")
for r in bf_html[:15]:
    print("HTML Rule:", r.strip()[:120])
