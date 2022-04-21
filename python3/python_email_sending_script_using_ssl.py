import logging
import sys
import smtplib
from email.mime.text import MIMEText


if len(sys.argv) != 6:
    print("\nLess or Unnecessary parameters")
else:
    # getting necessary values for email
    mailFrom = sys.argv[1]
    mailTo = sys.argv[2]
    password = sys.argv[3]
    subject = sys.argv[4]
    message = sys.argv[5]

    # making an object for email
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = mailFrom
    msg["To"] = mailTo
    print("\nthssubject ", subject)
    print("\nfrom ", mailFrom)
    print("\nto ", mailTo)
    print("\npassword ", password)
    print("\nmessage ", message)
    # creating and starting mail server
    try:
        s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        # s.starttls()
        s.login(mailFrom, password)  # authentication
        s.sendmail(mailFrom, mailTo, msg.as_string())  # sending mail
        s.quit()  # quitting
    except Exception as e:
        logging.error(exc_info=True)
        # print('\nError while sending mail')
