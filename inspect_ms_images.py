import re

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Check section.riva-ms
ms_match = re.search(r'<section[^>]*riva-ms[^>]*>.*?</section>', html, re.DOTALL)
if ms_match:
    ms_html = ms_match.group(0)
    print("Found riva-ms section, length:", len(ms_html))
    images = re.findall(r'<image[^>]*href="([^"]*)"[^>]*>', ms_html)
    print("SVG <image> hrefs:", images)
    img_tags = re.findall(r'<img[^>]*src="([^"]*)"[^>]*>', ms_html)
    print("Standard <img> srcs:", img_tags)
else:
    print("riva-ms not found")
