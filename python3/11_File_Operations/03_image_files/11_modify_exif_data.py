from PIL import Image
image = Image.open('cameraman.jpg')
image.save('cameraman_without_exif.jpg')