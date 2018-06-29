import imaplib
import email
imap = imaplib.IMAP4('mail.collab.net')
imap.login('leonardr', 'm4pl3r')
imap.select('Inbox')[1][0]

#Get the unique IDs for the messages in this folder.
uids = imap.uid('SEARCH', 'ALL')
print uids
uids = uids[1][0].split(' ')

#Get the first message.
messageText = imap.uid('FETCH', uids[0], "(RFC822)")[1][0][1]
message = email.message_from_string(messageText)
print message['Subject']
