fromAddress = 'sender@example.com'
toAddress = 'recipient@example.com'
msg = "Subject: Hello\n\nThis is the body of the message." 
import smtplib
server = smtplib.SMTP("localhost", 25)
server.sendmail(fromAddress, toAddress, ms
