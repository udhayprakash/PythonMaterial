from PIL import Image
 
img = Image.new('RGB', (60, 300), 
           color = (10, 255, 137))
img.save('pil_color.png')