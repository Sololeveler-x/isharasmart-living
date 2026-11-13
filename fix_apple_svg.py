with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Fix the single remaining #riva-house image in SVG
html = html.replace('href="#riva-house" xlink:href="#riva-house"/>', 'href="./img/works_with_apple.webp" xlink:href="./img/works_with_apple.webp"/>')

with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed Apple logo in SVG!")
