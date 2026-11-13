from PIL import Image

img = Image.open('home/img/ishara-logo.png')
w, h = img.size
print(f"Full image dimensions: {w}x{h}")

# Check where the logo is
# In the prompt metadata display, on the left is the square logo, on the right is the browser screenshot
# Let's see what the image looks like across X coordinates
# Let's save a crop of the left square
logo_box = (0, 0, min(w, h), h)
logo_crop = img.crop(logo_box)
logo_crop.save('home/img/ishara-logo-pure.png')
print(f"Saved logo crop: {logo_crop.size}")
