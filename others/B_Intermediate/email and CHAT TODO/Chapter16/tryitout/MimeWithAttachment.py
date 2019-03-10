from email.MIMEImage import MIMEImage
filename = "photo.jpg"
msg = MIMEImage(open(filename).read(), name=filename)
msg['From'] = 'Me <me@example.com>'
msg['To'] = 'You <you@example.com>'
msg['Subject'] = 'Your picture'
print str(msg)
