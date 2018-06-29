#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
textField = form.getfirst("textField")
radioButton = form.getfirst("radioButton")
submitButton = form.getfirst("button")

print 'Content-type: text/html\n'
print '<html>'
print '<body>'
print '<p>Here are the values of your form submission:</p>'
print '<ul>'
print '<li>In the text field, you entered "%s".</li>' % textField
print '<li>Of the radio buttons, you selected "%s".' % radioButton
print '<li>The name of the submit button you clicked is "%s".' % submitButton
print '</ul>'
print '</body>'
print '</html>'
