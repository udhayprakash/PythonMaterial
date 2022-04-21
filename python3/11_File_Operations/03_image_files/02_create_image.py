from PIL import Image

img = Image.new("RGB", (60, 300), color=(10, 100, 137))
#  R   G   B
img.save("pil_color.png")
