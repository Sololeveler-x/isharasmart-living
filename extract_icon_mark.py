from PIL import Image
import numpy as np

# Let's inspect ishara-logo-actual.png and crop just the icon mark
img = Image.open('home/img/ishara-logo-actual.png').convert('RGBA')
arr = np.array(img)
h, w = arr.shape[:2]

# The top part of the 150x150 logo (from y=0 to y=95) contains the stylized "i" with home and leaf!
# The bottom part (from y=95 to y=150) contains the text "ISHARA SMART LIVING"
icon_mark = img.crop((15, 8, 135, 95))
print("Icon mark size:", icon_mark.size)

# Create transparent icon mark
bg_color = arr[0, 0][:3]
icon_arr = np.array(icon_mark)
diff = np.sqrt(np.sum((icon_arr[:, :, :3].astype(float) - bg_color.astype(float))**2, axis=2))
alpha = np.where(diff < 22, 0, 255).astype(np.uint8)

icon_trans = icon_mark.copy()
icon_trans.putalpha(Image.fromarray(alpha, mode='L'))
icon_trans.save('home/img/ishara-icon-trans.png')
print("Saved clean icon mark to home/img/ishara-icon-trans.png")
