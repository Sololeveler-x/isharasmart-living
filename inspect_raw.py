import re
import base64

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print(f"HTML size: {len(html)} bytes")

# Check for riva sections
riva_classes = re.findall(r'class="([^"]*riva-[^"]*)"', html)
print(f"Found {len(riva_classes)} elements with 'riva-' classes")
unique_classes = set()
for c in riva_classes:
    for sub in c.split():
        if 'riva-' in sub:
            unique_classes.add(sub)
print("Unique riva classes:", sorted(list(unique_classes))[:30])

# Check for sections
sections = re.findall(r'<section[^>]*class="([^"]*)"[^>]*>', html)
print(f"Total sections: {len(sections)}")
for s in sections:
    print("Section:", s)

# Check for data: scripts
data_scripts = re.findall(r'src="(data:text/javascript;base64,[^"]*)"', html)
print(f"Total data: base64 scripts: {len(data_scripts)}")
for idx, s in enumerate(data_scripts):
    encoded = s.split('data:text/javascript;base64,')[1]
    decoded = base64.b64decode(encoded).decode('utf-8', errors='ignore')
    first_line = decoded.strip().split('\n')[0][:80]
    print(f" Script #{idx+1} ({len(decoded)} bytes): {first_line}")

# Check stylesheets
links = re.findall(r'<link[^>]*href="([^"]*)"[^>]*>', html)
for l in links:
    if '.css' in l:
        print("CSS link:", l)
