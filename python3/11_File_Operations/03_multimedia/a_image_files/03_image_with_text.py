from PIL import Image, ImageDraw

img = Image.new("RGB", (400, 30), color=(73, 109, 137))

d = ImageDraw.Draw(img)
d.text((10, 15), "Hello World", fill=(255, 255, 0))

img.save("images/pil_text.png")
