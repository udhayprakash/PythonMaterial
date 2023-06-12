"""
Purpose: CGI
    CGI - Common Gateway Interface

"""
import time

print("Content-Type: text/html\n\n")  # html markup follows
timeStr = time.strftime("%c")  # obtains complete current time
htmlFormat = """
<html>
<Title>The Time Now</Title>
<body>
<p>The current Central date and time is: {timeStr}</p>
</body>
</html> """
print(htmlFormat.format(**locals()))  # see embedded {timeStr} ^ above
