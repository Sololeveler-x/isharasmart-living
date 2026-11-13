from PIL import Image
import numpy as np

img = Image.open('home/img/ishara-logo-trans.png')
print("Mode:", img.mode, "Size:", img.size)
arr = np.array(img)
print("Alpha channel min/max/mean:", arr[:, :, 3].min(), arr[:, :, 3].max(), arr[:, :, 3].mean())
print("Corner (0,0) RGBA:", arr[0, 0])
print("Point (10,10) RGBA:", arr[10, 10])
print("Point (30,30) RGBA:", arr[30, 30])
