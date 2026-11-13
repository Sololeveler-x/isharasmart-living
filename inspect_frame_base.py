import base64
import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

data_scripts = re.findall(r'src="(data:text/javascript;base64,[^"]*)"', html)
s3 = data_scripts[2]
decoded = base64.b64decode(s3.split('data:text/javascript;base64,')[1]).decode('utf-8')

# Find where FRAME_BASE is defined and used
idx = decoded.find("FRAME_BASE")
if idx != -1:
    print(decoded[idx-50:idx+600])
