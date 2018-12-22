import logging 
from logging import handlers
import socket 
import traceback 

HOST = 'localhost'
FROM = '"Application Alert" <pythontutor@domain.com>'
TO   = 'you@domain.com'
SUBJECT = 'New critical Event from [APPLICATION]'

logging.basicConfig(level=logging.INFO)


handler = handlers.SMTPHandler(HOST, FROM, TO, SUBJECT)

email_logger = logging.getLogger('smtp.example')
email_logger.addHandler(handler)
email_logger.setLevel = logging.CRITICAL

logging.info('Roor logger output')

try:
    email_logger.critical('critical Event Notification\n\nTraceback:\n%s',
            ''.join(traceback.format_stack()))
except socket.error as error:
    logging.critical('Could not send email via SMTPHandler: %r', error)










