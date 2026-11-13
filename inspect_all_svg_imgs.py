with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

import re
images = re.findall(r'<image[^>]*>', html)
for i, img in enumerate(images):
    print(f"[{i+1}]: {repr(img)}")
