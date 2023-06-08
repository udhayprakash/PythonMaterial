from xmlrpc.server import SimpleXMLRPCServer


def get_info():
    return {"name": "John", "age": 30, "occupation": "Engineer"}


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(get_info, "info")

server.serve_forever()
