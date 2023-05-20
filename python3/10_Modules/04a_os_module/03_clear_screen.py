#!/usr/bin/python3
import os
from sys import platform


def ping_a_site(website_name):
    output = os.system(f"ping {website_name}")
    print(f"output:{output}")


def clear_screen():
    if platform == "win32":  # windows
        output = os.system("cls")
    else:
        output = os.system("clear")
    print("output", output)


def get_ip_info():
    if platform == "win32":
        output = os.system("ipconfig")
    else:
        output = os.system("ifconfig")
    print("output", output)


if __name__ == "__main__":
    clear_screen()
    print()
    ping_a_site("yahoo.com")

    print()
    ping_a_site("yahoo")

    clear_screen()
    # os.system('ipconfig')
    get_ip_info()
