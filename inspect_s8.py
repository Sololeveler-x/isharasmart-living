import base64
import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

data_scripts = re.findall(r'src="(data:text/javascript;base64,[^"]*)"', html)
s8 = data_scripts[7] # index 7 is 8th script
decoded = base64.b64decode(s8.split('data:text/javascript;base64,')[1]).decode('utf-8')
print("Script 8 length:", len(decoded))
print(decoded[:2000])
