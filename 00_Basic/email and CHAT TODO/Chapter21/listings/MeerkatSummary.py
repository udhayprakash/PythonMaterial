import xmlrpclib

class MeerkatSummary:
    """Lists channels that match a search term, in order of how many
    stories match."""

    SERVER_URL = 'http://www.oreillynet.com/meerkat/xml-rpc/server.php'

    def __init__(self):
        "Set up a reference to the Meerkat server."

        #Passing 'verbose=True' to the server constructor will make it
        #print the text of the request and response for each XML-RPC
        #call, letting you see the internal workings of the protocol.
        #verbose = True

        verbose = False
        server = xmlrpclib.ServerProxy(self.SERVER_URL, verbose=verbose)
        self.meerkat = server.meerkat

    def findChannels(self, searchTerm):
        "Given a search term, find out which channels have the most hits."
        channelTotals = {}
        items = self.meerkat.getItems({'search' : searchTerm,
                                       'channels' : True})
        for item in items:
            channel = item['channel']
            totalForChannel = channelTotals.get(channel, 0)
            totalForChannel += 1
            channelTotals[channel] = totalForChannel
        totalAndChannel = [(a,b) for b,a in channelTotals.items()]
        totalAndChannel.sort()
        totalAndChannel.reverse()
        print 'Meerkat report for "%s":' % searchTerm
        for total, channel in totalAndChannel:
            print "%2d %s" % (total, channel)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print "Usage: %s [search term]" % sys.argv[0]
        sys.exit(1)
    else:
        MeerkatSummary().findChannels(sys.argv[1])
