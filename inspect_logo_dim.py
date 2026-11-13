from PIL import Image

img = Image.open('home/img/ishara-logo.png')
print("Format:", img.format, "Size:", img.size, "Mode:", img.mode)
