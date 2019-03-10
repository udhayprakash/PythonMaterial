#!/usr/bin/python
from imaplib import IMAP4

class SubjectLister(IMAP4):
    """Connect to an IMAP4 mailbox and list the subject of every message
    in the mailbox."""

    def __init__(self, server, username, password):
        "Connect to the IMAP server."
        IMAP4.__init__(self, server)
        #Uncomment this line to see the details of the IMAP4 protocol.
        #self.debug = 4
        self.login(username, password)

    def summarize(self, mailbox='Inbox'):
        "Retrieve the subject of each message in the given mailbox."
        #The SELECT command makes the given mailbox the 'current' one,
        #and returns the number of messages in that mailbox. Each message
        #is accessible via its message number. If there are 10 messages
        #in the mailbox, the messages are numbered from 1 to 10.
        numberOfMessages = int(self._result(self.select(mailbox)))
        
        print '%s message(s) in mailbox "%s":' % (numberOfMessages, mailbox)

        #The FETCH command takes a comma-separated list of message
        #numbers, and a string designating what parts of the
        #message you want. In this case, we want only the
        #'Subject' header of the message, so we'll use an argument
        #string of '(BODY[HEADER.FIELDS (SUBJECT)])'.
        #
        #See section 6.4.5 of RFC3501 for more information on the
        #format of the string used to designate which part of the
        #message you want. To get the entire message, in a form
        #acceptable to the email parser, ask for '(RFC822)'.

        subjects = self._result(self.fetch('1:%d' % numberOfMessages,
                                         '(BODY[HEADER.FIELDS (SUBJECT)])'))
        for subject in subjects:
            if hasattr(subject, '__iter__'):
                subject = subject[1]                
                print '', subject[:subject.find('\n')]

    def _result(self, result):
        """Every method of imaplib returns a list containing a status
        code and a set of the actual result data. This convenience
        method throws an exception if the status code is other than
        "OK", and returns the result data if everything went all
        right."""
        status, result = result
        if status != 'OK':
            raise status, result
        if len(result) == 1:
            result = result[0]
        return result

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print 'Usage: %s [IMAP hostname] [IMAP user] [IMAP password]' % sys.argv[0]
        sys.exit(0)
    lister = SubjectLister(sys.argv[1], sys.argv[2], sys.argv[3])
    lister.summarize()
