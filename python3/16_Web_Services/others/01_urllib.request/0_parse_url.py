from urllib.parse import urlparse
o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
o   # ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', 
            # params='', query='', fragment='')
o.scheme  # 'http'
o.port    # 80
o.geturl() # 'http://www.cwi.nl:80/%7Eguido/Python.html'

'''
 >>> urlparse('//www.cwi.nl:80/%7Eguido/Python.html')
 ParseResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
            params='', query='', fragment='')
 >>> urlparse('www.cwi.nl/%7Eguido/Python.html')
 ParseResult(scheme='', netloc='', path='www.cwi.nl/%7Eguido/Python.html',
            params='', query='', fragment='')
 >>> urlparse('help/Python.html')
 ParseResult(scheme='', netloc='', path='help/Python.html', params='',
            query='', fragment='')

>>> u = urlparse('//www.cwi.nl:80/%7Eguido/Python.html')
>>> u
ParseResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
            params='', query='', fragment='')
>>> u._replace(scheme='http')
ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
            params='', query='', fragment='')


from urllib.parse import urljoin
>>> urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')
'http://www.cwi.nl/%7Eguido/FAQ.html'

>>> urljoin('http://www.cwi.nl/%7Eguido/Python.html',
...         '//www.python.org/%7Eguido')
'http://www.python.org/%7Eguido'



>>> from urllib.parse import urlsplit
>>> url = 'HTTP://www.Python.org/doc/#'
>>> r1 = urlsplit(url)
>>> r1.geturl()
'http://www.Python.org/doc/'
>>> r2 = urlsplit(r1.geturl())
>>> r2.geturl()
'http://www.Python.org/doc/'

'''