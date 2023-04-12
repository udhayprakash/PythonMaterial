import json


def lambda_handler(event, context):
    # return 'Hello, world!'  # string
    # return 42 # int
    # return 42.43 # float

    # return None # None
    # return True  # bool

    # return ['Hello', 'world!', 3]  # list
    # return ('Hello', 'world!', 3)  # tuple
    # return {'Hello', 'world!', 3}  # set

    # return {"name": "Gudo", "age": 78}  # dict

    return json.dumps(
        {
            "int": 12,
            "float": 2132.21,
            "bool": True,
            "None": None,
            "string": "Hello",
            "list": [11, 22, 33],
            "tuple": (11, 22, 33),
            # "set": {11, 22, 33, 11, 22, 33},
            "dict": {"a": 1, "b": 2},
        }
    )
