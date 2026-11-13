import base64
import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

data_scripts = re.findall(r'src="(data:text/javascript;base64,[^"]*)"', html)
s3 = data_scripts[2] # 3rd script is index 2
decoded = base64.b64decode(s3.split('data:text/javascript;base64,')[1]).decode('utf-8')
print("Script 3 length:", len(decoded))
# Look for brand mentions or URLs
urls = re.findall(r'https?://[^\s"\'>]+', decoded)
print("URLs in Script 3:", urls)
riva_mentions = re.findall(r'.{0,30}riva.{0,30}', decoded, re.IGNORECASE)
print(f"Riva mentions in Script 3 ({len(riva_mentions)}):")
for r in riva_mentions[:10]:
    print(" -", r.strip())
