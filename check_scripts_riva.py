import base64
import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

data_scripts = re.findall(r'src="(data:text/javascript;base64,[^"]*)"', html)
for i, s in enumerate(data_scripts):
    b64 = s.split('data:text/javascript;base64,')[1]
    decoded = base64.b64decode(b64).decode('utf-8', errors='ignore')
    if 'riva' in decoded.lower():
        print(f"Script #{i+1} mentions riva ({len(decoded)} bytes)")
        matches = re.findall(r'.{0,30}riva.{0,30}', decoded, re.IGNORECASE)
        for m in matches[:5]:
            print("   ->", m.strip())
