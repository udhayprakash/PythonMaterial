#!/usr/bin/env python
# encoding: utf-8
from wand.image import Image

with Image(filename='mona-lisa.png') as img:
    print img.format
    with img.convert('jpeg') as converted:
        converted.save(filename='outputimage.jpg')
        converted.resize(72,72)
        converted.save(filename='outputimage_thumbnail.jpg')