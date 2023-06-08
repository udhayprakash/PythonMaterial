from xmlrpc.server import SimpleXMLRPCServer


def say_hello():
    return "Hello, XML-RPC!"


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(say_hello, "hello")

server.serve_forever()
