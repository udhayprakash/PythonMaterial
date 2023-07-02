from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = request.form["num1"]
    num2 = request.form["num2"]
    operation = request.form["operation"]

    if not num1 or not num2:
        result = "Please enter two numbers."
    elif not num1.isdigit() or not num2.isdigit():
        result = "Please enter valid numbers."
    elif operation == "add":
        result = int(num1) + int(num2)
    elif operation == "subtract":
        result = int(num1) - int(num2)
    elif operation == "multiply":
        result = int(num1) * int(num2)
    elif operation == "divide":
        if num2 == "0":
            result = "Cannot divide by zero."
        else:
            result = int(num1) / int(num2)
    else:
        result = "Invalid operation."

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run()
