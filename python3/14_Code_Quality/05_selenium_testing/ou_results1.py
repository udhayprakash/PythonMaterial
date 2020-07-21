import mechanize

br = mechanize.Browser()
br.open("http://www.osmania.ac.in/res07/20180472.jsp")
br.select_form(nr=0)
br.form['htno'] = '160314732001'
req = br.submit()
print(req)
