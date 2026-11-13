with open('tour/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    t = f.read()

t = t.replace('rivasmart_logo_reversed.png', 'ishara-logo-trans.png')
t = t.replace('rivasmart_logo.png', 'ishara-logo-trans.png')
t = t.replace('alt="RiVaSmart"', 'alt="Ishara Smart Living"')

# Favicon in tour
if '<head>' in t:
    t = t.replace('<head>', '<head>\n<link rel="icon" type="image/png" href="./ishara-logo-trans.png">')

with open('tour/index.html', 'w', encoding='utf-8') as f:
    f.write(t)

print("Updated tour/index.html with official Ishara logo!")
