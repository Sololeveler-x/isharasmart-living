import re

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

m = re.search(r'<svg[^>]*riva-ms-svg[^>]*>.*?</svg>', html, re.DOTALL)
if m:
    svg_txt = m.group(0)
    images = re.findall(r'<image[^>]*>', svg_txt)
    for i, img in enumerate(images):
        print(f"[{i+1}]: {repr(img)}")
