import smtplib

from email import message

message = message.EmailMessage()
message.set_content('Message content here')
message['Subject'] = 'Your subject here'
message['From'] = 'me@example.com'
message['To'] = 'user@example.com'

smtp_server = smtplib.SMTP('smtp.server.address:587')
smtp_server.send_message(message)
smtp_server.quit()