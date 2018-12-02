from PIL import Image
 
img = Image.new('RGB', (60, 30), color = (173, 109, 137))
img.save('pil_color.png')