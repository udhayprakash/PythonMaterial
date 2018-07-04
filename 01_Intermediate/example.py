from requests import get
from re import compile

html = get( 'http://www.ancebergamo.it/schedaimpresa.asp?idimpresa=1263')
text = html.text
textRegex = compile(r'<title>(.*)</title>')
data = textRegex.search(text)
print 'data.group()', data.group()
print 'data.group(0)', data.group(0)
