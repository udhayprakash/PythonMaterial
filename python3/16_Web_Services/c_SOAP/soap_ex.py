#!/usr/bin/python
"""
Purpose: Consuming SOAP interface API

    pip install -U zeep --user

python -m zeep http://www.dneonline.com/calculator.asmx?wsdl

"""

from zeep import Client


def calculator_soap_service(num1, num2):
    wsdl_url = "http://www.dneonline.com/calculator.asmx?wsdl"
    cl = Client(wsdl_url)

    addition = cl.service.Add(num1, num2)
    print(f"addition    :{addition:5}")

    division = cl.service.Divide(num1, num2)
    print(f"division    :{division:5}")

    multiply = cl.service.Multiply(num1, num2)
    print(f"multiply    :{multiply}:5")

    subtraction = cl.service.Subtract(num1, num2)
    print(f"subtraction :{subtraction}:5")


if __name__ == "__main__":
    calculator_soap_service(10, 30)
