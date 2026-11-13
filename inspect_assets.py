import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

imgs = re.findall(r'<img[^>]*src="([^"]*)"', html)
print(f"Total img src: {len(imgs)}")
unique_imgs = set(imgs)
for u in sorted(list(unique_imgs)):
    print("IMG:", u)

videos_webm = re.findall(r'data-webm="([^"]*)"', html)
print("Videos data-webm:", videos_webm)

videos_mp4 = re.findall(r'data-mp4="([^"]*)"', html)
print("Videos data-mp4:", videos_mp4)

posters = re.findall(r'data-bg="([^"]*)"', html)
print("Hero data-bg posters:", posters)
