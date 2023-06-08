from xmlrpc.server import SimpleXMLRPCServer


def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero")
    return x / y


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(divide, "divide")

server.serve_forever()
