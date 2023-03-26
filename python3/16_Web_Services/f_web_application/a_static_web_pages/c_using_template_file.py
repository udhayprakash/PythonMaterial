def fileToStr(fileName):  # NEW
    """Return a string containing the contents of the named file."""
    fin = open(fileName)
    contents = fin.read()
    fin.close()
    return contents


def main():
    person = input("Enter a name: ")  # NEW
    contents = fileToStr("c_helloTemplate.html").format(**locals())  # NEW
    browseLocal(contents, "c_helloPython3.html")  # NEW filename


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
