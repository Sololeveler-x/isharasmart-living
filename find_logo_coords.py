from PIL import Image
import numpy as np

img = Image.open('C:/Users/JEEVAN/.gemini/antigravity-ide/brain/tempmediaStorage/media_1792764099526.png')
w, h = img.size
print(f"Original size: {w}x{h}")

arr = np.array(img)
# Sample points across horizontal line at h//2
print("Row at middle h//2 every 50px:")
for x in range(0, w, 50):
    print(f" x={x}: {arr[h//2, x][:3]}")
