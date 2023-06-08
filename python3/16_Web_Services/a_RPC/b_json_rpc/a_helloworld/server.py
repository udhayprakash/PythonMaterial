# pip install jsonrpcserver async-json-rpc jsonrpcserver[asyncio]

from jsonrpcserver import method


# ----------------METHOD 1------------
@method
def say_hello():
    return "Hello, JSON-RPC!"


methods = [say_hello]

# ----------------METHOD 2------------
from jsonrpcserver import methods
from jsonrpcserver.async_methods import Methods

methods = Methods()

methods.add(say_hello)

# ----------------METHOD 3------------
from jsonrpcserver import async_methods

methods = async_methods.Methods()
methods.add(say_hello)
