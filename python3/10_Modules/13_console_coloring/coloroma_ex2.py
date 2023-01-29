#!usr/bin/env python

import os
import sys

from colorama import AnsiToWin32, Back, Fore, Style, init

"""
    colorama.Fore -> To color the foreground color
    colorama.Back -> To color the Background color
    colorama.Style -> To color the text style
"""


def main():
    print(Fore.YELLOW + "This is YELLOW TEXT!")
    print(Back.WHITE + Fore.BLUE + "This is BLUE TEXT!")
    print(Back.BLUE + Fore.YELLOW + "This is YELLOW TEXT!" + Fore.RED + "RED!")

    print(Style.NORMAL)
    print(Back.BLUE + Fore.YELLOW + "This is YELLOW TEXT!" + Fore.RED + "RED!")
    print(Style.DIM)
    print(Back.BLUE + Fore.YELLOW + "This is YELLOW TEXT!" + Fore.RED + "RED!")
    print(Style.BRIGHT)
    print(Back.BLUE + Fore.YELLOW + "This is YELLOW TEXT!" + Fore.RED + "RED!")
    # Back.RESET is used when autoreset is not used
    print(Fore.WHITE + "This is WHITE TEXT!" + Back.RESET)
    print(Fore.CYAN + "This is CYAN TEXT!")
    print(Back.BLACK)  # Reseting Background color to black
    print(Fore.GREEN + "This is GREEN TEXT!")
    print(Fore.LIGHTBLUE_EX + "This is LIGHTBLUE_EX TEXT!")
    # raw_input("Enter something:: ")  #stdout will have latest foreground
    # color
    print(Fore.MAGENTA + "This is MAGENTA TEXT!")

    init(wrap=False)
    stream = AnsiToWin32(sys.stderr).stream
    print(Fore.BLUE + "blue text on stderr", file=stream)


if __name__ == "__main__":
    if "win" in sys.platform:
        os.system("cls")
        init()
    else:
        os.system("clear")
    # init(autoreset=True) # To reset the color to defaults, for every statement
    # init(convert = True) # works in the same way as init()
    # init(convert = False) # Used when we want to stop the color change
    # init(wrap = True)# works in the same way as init()
    # init(convert = False) # Used when we want to stop the color change
    main()
