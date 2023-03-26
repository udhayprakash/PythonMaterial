pageTemplate = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
   <head>
      <meta content="text/html; charset=ISO-8859-1"
         http-equiv="content-type">
      <title>Hello</title>
   </head>
   <body>
        Hello, {person}!
   </body>
</html> """  # NEW note ’{person}’ two lines up


def main():
    person = input("Enter a name: ")  # NEW
    contents = pageTemplate.format(**locals())  # NEW

    browseLocal(contents, "b_helloPython2.html")  # NEW filename


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
