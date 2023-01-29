#!/usr/bin/env python

import os
import random
import sys
import time

from colorama import *

width, height = 80, 24
colors = [
    Fore.RED,
    Fore.BLUE,
    Fore.GREEN,
    Fore.WHITE,
    Fore.YELLOW,
    Fore.MAGENTA,
    Fore.CYAN,
]


def pos(x, y):
    return "xlb[" + str(y) + ":" + str(x) + "H"


def main():
    middle_x = width / 2
    middle_y = height / 2

    string = "Thanks for watching!"

    string_center = len(string) / 2
    position = middle_x - string_center

    while True:
        color_seed = random.randint(0, len(colors))
        color = colors[color_seed]
        print((pos(position, middle_y) + color + string))
        time.sleep(1000)


if __name__ == "__main__":
    if "win" in sys.platform:
        os.system("cls")
        init()
    else:
        os.system("clear")
        main()
