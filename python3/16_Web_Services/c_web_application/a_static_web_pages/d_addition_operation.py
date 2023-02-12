def fileToStr(fileName):  # NEW
    """Return a string containing the contents of the named file."""
    fin = open(fileName)
    contents = fin.read()
    fin.close()
    return contents


# def main():
#     person = input("Enter a name: ") # NEW
#     contents = fileToStr("helloTemplate.html").format(**locals()) # NEW
#     browseLocal(contents, "helloPython3.html") # NEW filename


def processInput(numStr1, numStr2):  # NEW
    """Process input parameters and return the final page as a string."""
    num1 = int(numStr1)  # transform input to output data
    num2 = int(numStr2)
    total = num1 + num2
    return fileToStr("d_addition_operation.html").format(**locals())


def main():  # NEW
    numStr1 = input("Enter an integer: ")  # obtain input
    numStr2 = input("Enter another integer: ")
    contents = processInput(numStr1, numStr2)  # process input into a page
    browseLocal(contents, "helloPython3.html")  # display page


def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename, "w")
    output.write(text)
    output.close()


def browseLocal(webpageText, filename):
    """Start your webbrowser on a local file containing the text."""
    strToFile(webpageText, filename)
    import webbrowser

    webbrowser.open(filename)


main()
