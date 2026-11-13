from PIL import Image

img = Image.open('C:/Users/JEEVAN/.gemini/antigravity-ide/brain/ef3d38ba-0182-42c8-b2fb-2c98254675e1/.user_uploaded/media_1792763460960.png')
print("Image 1792763460960:", img.format, img.size, img.mode)

# Save to home/img/
img.save('home/img/ishara-logo-actual.png')
print("Saved to home/img/ishara-logo-actual.png")
