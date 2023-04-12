import json


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


def fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    else:
        fib = [0, 1]
        while len(fib) < num:
            fib.append(fib[-1] + fib[-2])
        return fib


def lambda_handler(event, context):
    n = int(event["n"])

    return {
        "statusCode": 200,
        "result": json.dumps({"factorial": factorial(n), "fibonacci": fibonacci(n)}),
    }


"""
event Data
{
    "n": 5
}
"""
