from PIL import Image
import numpy as np

# Load the original user uploaded logo
p = r'C:\Users\JEEVAN\.gemini\antigravity-ide\brain\ef3d38ba-0182-42c8-b2fb-2c98254675e1\.user_uploaded\media_1792763460960.png'
im = Image.open(p).convert('RGBA')
arr = np.array(im)

# Detect background color from corners
bg = arr[0, 0][:3].astype(float)
diff = np.sqrt(np.sum((arr[:, :, :3].astype(float) - bg)**2, axis=2))

# 1. Pure Icon Mark: rows 28 to 84, cols 50 to 98
icon_arr = arr[28:85, 50:99].copy()
icon_diff = diff[28:85, 50:99]
icon_alpha = np.where(icon_diff < 20, 0, 255).astype(np.uint8)
icon_im = Image.fromarray(icon_arr)
icon_im.putalpha(Image.fromarray(icon_alpha, mode='L'))
# Crop to exact non-transparent bounding box with 2px padding
bbox = icon_im.getbbox()
print("Icon bbox:", bbox)
icon_im = icon_im.crop(bbox)
# Add 4px transparent padding around icon
padded_icon = Image.new('RGBA', (icon_im.width + 8, icon_im.height + 8), (0, 0, 0, 0))
padded_icon.paste(icon_im, (4, 4))
padded_icon.save('home/img/ishara-icon-pure.png')
print("Saved ishara-icon-pure.png:", padded_icon.size)

# 2. Complete full logo: rows 28 to 117, cols 20 to 131
full_arr = arr[28:118, 20:132].copy()
full_diff = diff[28:118, 20:132]
full_alpha = np.where(full_diff < 20, 0, 255).astype(np.uint8)
full_im = Image.fromarray(full_arr)
full_im.putalpha(Image.fromarray(full_alpha, mode='L'))
bbox_full = full_im.getbbox()
full_im = full_im.crop(bbox_full)
padded_full = Image.new('RGBA', (full_im.width + 12, full_im.height + 12), (0, 0, 0, 0))
padded_full.paste(full_im, (6, 6))
padded_full.save('home/img/ishara-logo-full-trans.png')
print("Saved ishara-logo-full-trans.png:", padded_full.size)

# Also check original rivasmart-logo.webp dimensions
riva_logo = Image.open('home/img/rivasmart-logo.webp')
print("rivasmart-logo.webp size:", riva_logo.size)
