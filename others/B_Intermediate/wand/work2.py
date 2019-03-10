from wand.image import Image

with Image(filename="rose:") as rose:
    x = 0
    chunk_size = 10
    while True:
        try:
            with rose[x:x+chunk_size, 0:rose.height] as chunk:
                chunk.save(filename='rose_{0}.png'.format(x))
                x += chunk_size
        except IndexError:
            break