from PIL import Image

# 0 - 255

img = Image.new("RGB", (60, 300), color=(10, 100, 137))
#                                         R   G   B

img.save("images/pil_color.png")
