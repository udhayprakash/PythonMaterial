from colorama import Back, Fore, Style, colorama_text

print(Fore.RED + "some red text")
print(Back.GREEN + "and with a green background")
print(Style.DIM + "and in dim text")
print(Style.RESET_ALL)
print("back to normal now")
print()

with colorama_text():
    print(Fore.GREEN + "text is green")
    print(Fore.RESET + "text is back to normal")

print("text is back to stdout")

# Ref - more examples - https://github.com/tartley/colorama/blob/master/demos/
