#!/usr/bin/python
import sys
import SimpleXMLRPCServer
from BittyWiki import Wiki

class BittyWikiAPI:
    """A simple wrapper around the basic BittyWiki functionality we
    want to expose to the API."""

    def __init__(self, wikiBase):
        "Initialize a wiki located in the given directory."
        self.wiki = Wiki(wikiBase)

    def getPage(self, pageName):
        "Returns the text of the given page."
        page = self.wiki.getPage(pageName)
        if not page.exists():
            raise NoSuchPage, page.name
        return page.getText()

    def save(self, pageName, newText):
        "Saves a page of the wiki."
        page = self.wiki.getPage(pageName)
        page.text = newText
        page.save()
        return "Page saved."

    def delete(self, pageName):
        "Deletes a page of the wiki."
        page = self.wiki.getPage(pageName)
        if not page.exists():
            raise NoSuchPage, pageName
        page.delete()
        return "Page deleted."                    

class NoSuchPage(Exception):
    pass

def handlerSetup(handler, api):
    """This function registers the methods of the BittyWiki API
    as functions of an XML-RPC handler."""

    #Register the standard functions used by XML-RPC to advertise which methods
    #are available on a given server.
    handler.register_introspection_functions()

    #Register the BittyWiki API methods as XML-RPC functions in the
    #'bittywiki' namespace.
    handler.register_function(api.getPage, 'bittywiki.getPage')
    handler.register_function(api.save, 'bittywiki.save')
    handler.register_function(api.delete, 'bittywiki.delete')

    #Here's a way of registering all three methods in one line of
    #code, by registering the API object itself. It's commented out
    #because it exposes a security hole in older versions of Python
    #(specifically: 2.2, 2.3.4 and 2.4.0). See
    #http://www.python.org/security/PSF-2005-001/ for details.
    #
    #handler.register_instance(api)
    #
    #Note also that when you do this, the functions exposed to XML-RPC
    #will not have the 'bittywiki.' prefix: they'll be named,
    #e.g. "getPage" instead of "bittywiki.getPage". If this disturbs
    #you, try something like this instead:
    #class Container:
    #    pass
    #container = Container()
    #container.bittywiki = api
    #handler.register_instance(container)


if __name__ == '__main__':
    WIKI_BASE = 'wiki/'
    api = BittyWikiAPI(WIKI_BASE)
    standalonePort = None
    if len(sys.argv) > 1:
        #The user provided a port number; that means they want to
        #run a standalone server.
        standalonePort = sys.argv[1]
        try:
            standalonePort = int(standalonePort)
        except ValueError:
            #Oops, that wasn't a port number. Chide the user and exit.
            scriptName = sys.argv[0]
            print 'Usage:'
            print ' "%s [port number]" to start a standalone server.' \
                  % scriptName
            print ' "%s" to invoke as a CGI.' % scriptName
            sys.exit(1)
        isStandalone = 1
        print "Starting up standalone XML-RPC server on port %s." \
              % standalonePort
        handler = SimpleXMLRPCServer.SimpleXMLRPCServer\
                  (('localhost', standalonePort))
    else:
        #No port number specified; this is a CGI invocation.
        handler = SimpleXMLRPCServer.CGIXMLRPCRequestHandler()

    #The function registration step is identical for
    #SimpleXMLRPCServer and CGIXMLRPCRequestHandler.
    handlerSetup(handler, api)

    if standalonePort:
        handler.serve_forever()
    else:
        handler.handle_request()
