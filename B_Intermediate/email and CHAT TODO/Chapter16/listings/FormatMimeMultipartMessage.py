#!/usr/bin/python
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

import os
import sys

# filename = sys.argv[1]

msg = MIMEMultipart()
msg['From'] = 'Me <bifrophoth@qwfox.com>'
msg['To'] = 'You <l2378435@nwytg.com>'
msg['Subject'] = 'Your picture'

text = MIMEText("Here's that picture I took of you.")
msg.attach(text)


# image = MIMEImage(open(filename).read(), name=os.path.split(filename)[1])
# msg.attach(image)
print str(msg)
