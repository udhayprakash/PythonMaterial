#!/usr/bin/python
from poplib import POP3
import email
class SubjectLister(POP3):

    """Connect to a POP3 mailbox and list the subject of every message
    in the mailbox."""

    def __init__(self, server, username, password):
        "Connect to the POP3 server."
        POP3.__init__(self, server, 110)
        #Uncomment this line to see the details of the POP3 protocol.
        #self.set_debuglevel(2)
        self.user(username)
        response = self.pass_(password)
	if response[:3] == '+OK':
            #There was a problem connecting to the server.
            raise Exception, response	

    def summarize(self):
        "Retrieve each message, parse it, and print the subject."
        numMessages = self.stat()[0]
        print '%d message(s) in this mailbox.' % numMessages
	parser = email.Parser.Parser()
        for messageNum in range(1, numMessages+1):
	    messageString = '\n'.join(self.top(messageNum, 0)[1])
            message = parser.parsestr(messageString)
            #Passing in True to parser.parsestr() will only parse the headers
            #of the message, not the body. Since all we care about is the
            #body, this will save some time. However, this is only
            #supported in Python 2.2.2 and up.
            #message = parser.parsestr(messageString, True)
	    print '', message['Subject']

class TopBasedSubjectLister(SubjectLister):

    def summarize(self):
        """Retrieve the first part of the message and find the 'Subject:'
        header."""
        print '%d message(s) in this mailbox.' % self.numMessages
        for messageNum in range(1, self.numMessages+1):
            #Just get the headers of each message. Scan the headers
            #looking for the subject.
            for header in self.top(messageNum, 0)[1]:
                if header.find('Subject:') == 0:
                    print header[len('Subject:'):]
                    break

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print 'Usage: %s [POP3 hostname] [POP3 user] [POP3 password]' % sys.argv[0]
        sys.exit(0)
    lister = TopBasedSubjectLister(sys.argv[1], sys.argv[2], sys.argv[3])
    lister.summarize()
