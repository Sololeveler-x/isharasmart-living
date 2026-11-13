from PIL import Image
import numpy as np

img = Image.open('home/img/ishara-logo-pure.png').convert('RGBA')
arr = np.array(img)

# Check corner color (the background color of the logo)
corner_color = arr[10, 10]
print("Corner color:", corner_color)

# Make transparent version by keying out the light off-white background (#fbf7f0 approx)
# Background is approximately (251, 247, 240)
# We can calculate distance from corner color
diff = np.sqrt(np.sum((arr[:, :, :3].astype(float) - corner_color[:3].astype(float))**2, axis=2))
alpha = np.where(diff < 25, 0, 255).astype(np.uint8)

# Feather edges slightly
mask_img = Image.fromarray(alpha, mode='L')
transparent_logo = img.copy()
transparent_logo.putalpha(mask_img)
transparent_logo.save('home/img/ishara-logo-transparent.png')
print("Saved transparent logo:", transparent_logo.size)

# Also copy both to tour/ and home/
img.save('home/logo.png')
img.save('tour/logo.png')
transparent_logo.save('tour/logo-transparent.png')
