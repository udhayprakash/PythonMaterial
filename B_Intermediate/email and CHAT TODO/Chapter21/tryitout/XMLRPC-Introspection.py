import xmlrpclib
server = xmlrpclib.ServerProxy("http://localhost:8001/")
server.system.listMethods()
server.system.methodHelp("bittywiki.save")
server.system.methodSignature("bittywiki.save")
