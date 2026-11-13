with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

html = html.replace(
    '<image width="1200" height="500" href="./img/works_with_alexa.webp" xlink:href="./img/works_with_alexa.webp"/>',
    '<image width="1200" height="500" href="./img/works_with_apple.webp" xlink:href="./img/works_with_apple.webp"/>'
)

with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Changed [1] to works_with_apple.webp!")
