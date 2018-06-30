#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os
import re
from BittyWiki import Wiki, Page, NotWikiWord

class WikiRestApiCGI:

    #The possible operations on a wiki page.
    VIEW = ''
    WRITE = 'write'
    DELETE = 'delete'

    #The possible response codes this application might return.
    RESPONSE_CODES = { 200 : 'OK',
                       400 : 'Bad Request',
                       404 : 'Not Found'}
    
    def __init__(self, wikiBase):
        "Initialize with the given wiki."
        self.wiki = Wiki(wikiBase)

    def run(self):
        """Determine the command, dispatch to the appropriate handler,
        and print the results as an XML document."""
        toDisplay = None
        try:
            page = os.environ.get('PATH_INFO', '')
            if page:
                page = page[1:]
            page = self.wiki.getPage(page)
        except NotWikiWord, badName:
            toDisplay = 400, '"%s" is not a valid wiki page name.' % badName

        if not toDisplay:
            form = cgi.FieldStorage()
            operation = form.getfirst('operation', self.VIEW)
            operationMethod = self.OPERATION_METHODS.get(operation)
            if operationMethod:
                if not page.exists() and operation != self.WRITE:
                    toDisplay = 404, 'No such page: "%s"' % page.name
                else:
                    toDisplay = operationMethod(self, page, form)
            else:
                toDisplay = 400, '"%s" is not a valid operation.' % operation
                
        #Print the response.
        responseCode, payload = toDisplay
        print 'Status: %s %s' % (responseCode,
                                 self.RESPONSE_CODES.get(responseCode))
        print 'Content-type: text/plain\n'
        print payload

    def viewOperation(self, page, form=None):
        "Returns the raw text of the given wiki page."
        return 200, page.getText()
    
    def writeOperation(self, page, form):
        "Writes the specified page."
        page.text = form.getfirst('data')
        page.save()
        return 200, "Page saved."
    
    def deleteOperation(self, page, format, form=None):
        "Deletes the specified page."
        if not page.exists():
            toDisplay = 404, "You can't delete a page that doesn't exist."
        else:
            page.delete()
            toDisplay = 200, "Page deleted."
        return toDisplay

    #A registry mapping 'operation' keys to methods that perform the operations.
    OPERATION_METHODS = { VIEW : viewOperation,
                          WRITE: writeOperation,
                          DELETE: deleteOperation }

if __name__ == '__main__':
    WikiRestApiCGI('wiki/').run()
