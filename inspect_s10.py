import base64
import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

data_scripts = re.findall(r'src="(data:text/javascript;base64,[^"]*)"', html)
s10 = data_scripts[9] # 10th script is index 9
decoded = base64.b64decode(s10.split('data:text/javascript;base64,')[1]).decode('utf-8')
print("Script 10 length:", len(decoded))
print(decoded[:1000])
