import xmlrpclib
server = xmlrpclib.ServerProxy("http://localhost:8001/")
#Alternatively, something like:
#server = xmlrpclib.ServerProxy("http://localhost/cgi-bin/bittywiki-xmlrpc.cgi")
bittywiki = server.bittywiki
bittywiki.getPage("CreatedByXMLRPC")
bittywiki.save("CreatedByXMLRPC", "This page was created through the XML-RPC interface.")
bittywiki.getPage("CreatedByXMLRPC")
