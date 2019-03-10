from wand.image import Image
with Image(filename='mona-lisa.png') as img:
    img.type = 'grayscale';
    img.save(filename='grayscale.jpg');