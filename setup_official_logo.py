from PIL import Image
import numpy as np

img = Image.open('home/img/ishara-logo-actual.png')
print("Size:", img.size, "Mode:", img.mode)

arr = np.array(img)
print("Top-left pixel (corner):", arr[0, 0])
print("Middle pixel:", arr[75, 75])

# Save as official logo files
img.save('home/img/ishara-logo.png')
img.save('home/logo.png')
img.save('tour/ishara-logo.png')
img.save('tour/logo.png')

# Create a transparent version by removing background
bg_color = arr[0, 0][:3]
diff = np.sqrt(np.sum((arr[:, :, :3].astype(float) - bg_color.astype(float))**2, axis=2))
alpha = np.where(diff < 20, 0, 255).astype(np.uint8)

trans_img = img.copy()
trans_img.putalpha(Image.fromarray(alpha, mode='L'))
trans_img.save('home/img/ishara-logo-trans.png')
trans_img.save('tour/ishara-logo-trans.png')
print("Saved transparent logo!")
