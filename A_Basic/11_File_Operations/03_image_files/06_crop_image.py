from PIL import Image

original_image = Image.open("strawberries.png")
original_image.show()

x1,y1, x2, y2 = 100, 100, 300, 300 # x and y coordinates relative to top left corner
cropped_image = original_image.crop((x1,y1, x2, y2))
cropped_image.show()
