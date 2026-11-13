import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

images_raw = re.findall(r'<image[^>]*>', raw)
for img in images_raw:
    print(img)
