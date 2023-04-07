import json


def lambda_handler(event, context):
    temperature = event["temperature"]
    if event["unit"] == "C":
        return f"{temperature} degrees Celsius is {temperature * 9/5 + 32} degrees Fahrenheit"
    elif event["unit"] == "F":
        return f"{temperature} degrees Fahrenheit is {(temperature - 32) * 5/9} degrees Celsius"
    else:
        return "Invalid unit. Use 'C' or 'F'."


"""
event Data:
    {
    "temperature": 32,
    "unit": "C"
    }

"""
