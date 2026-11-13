import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

m = re.search(r'<section[^>]*riva-ms[^>]*>.*?</section>', raw, re.DOTALL)
if m:
    print("Found riva-ms in raw/home.html, len:", len(m.group(0)))
    raw_svg = m.group(0)
    imgs = re.findall(r'<image[^>]*>', raw_svg)
    for i, img in enumerate(imgs):
        print(f"RAW [{i+1}]: {repr(img)}")
