from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", "/home/user", perm="elradfmw")
authorizer.add_anonymous("/home/nobody")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()

180000 + 180000 * 0.15 = 207000
207000 + 207000 * 0.40 = 289800

180000 + 180000 * 0.60 = 288000
