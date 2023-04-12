from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for the API
chips = [
    {
        "chip_id": 1,
        "chip_name": "Intel Core i7-11700K",
        "manufacturer": "Intel",
        "year_of_manufacture": 2021,
        "transistor_count": 17400000,
    },
    {
        "chip_id": 2,
        "chip_name": "AMD Ryzen 9 5950X",
        "manufacturer": "AMD",
        "year_of_manufacture": 2020,
        "transistor_count": 16600000,
    },
    {
        "chip_id": 3,
        "chip_name": "Nvidia GeForce RTX 3080",
        "manufacturer": "Nvidia",
        "year_of_manufacture": 2020,
        "transistor_count": 28000000,
    },
]

transistors = [
    {
        "transistor_id": 1,
        "chip_id": 1,
        "gate_type": "FinFET",
        "material": "Silicon",
        "size": "10 nm",
    },
    {
        "transistor_id": 2,
        "chip_id": 1,
        "gate_type": "FinFET",
        "material": "Silicon",
        "size": "10 nm",
    },
    {
        "transistor_id": 3,
        "chip_id": 2,
        "gate_type": "FinFET",
        "material": "Silicon",
        "size": "7 nm",
    },
    {
        "transistor_id": 4,
        "chip_id": 2,
        "gate_type": "FinFET",
        "material": "Silicon",
        "size": "7 nm",
    },
    {
        "transistor_id": 5,
        "chip_id": 3,
        "gate_type": "FinFET",
        "material": "Silicon",
        "size": "8 nm",
    },
    {
        "transistor_id": 6,
        "chip_id": 3,
        "gate_type": "FinFET",
        "material": "Silicon",
        "size": "8 nm",
    },
]

revenue = [
    {"revenue_id": 1, "chip_id": 1, "date": "2021-03-01", "amount": 100000},
    {"revenue_id": 2, "chip_id": 2, "date": "2021-03-02", "amount": 200000},
    {"revenue_id": 3, "chip_id": 3, "date": "2021-03-03", "amount": 300000},
]


# Endpoint for getting all chips
@app.route("/chips", methods=["GET"])
def get_chips():
    return jsonify({"chips": chips})


# Endpoint for getting a specific chip
@app.route("/chips/<int:chip_id>", methods=["GET"])
def get_chip(chip_id):
    chip = [chip for chip in chips if chip["chip_id"] == chip_id]
    return jsonify({"chip": chip})


# Endpoint for getting all transistors for a specific chip
@app.route("/chips/<int:chip_id>/transistors", methods=["GET"])
def get_transistors(chip_id):
    chip_transistors = [
        transistor for transistor in transistors if transistor["chip_id"] == chip_id
    ]
    return jsonify({"transistors": chip_transistors})


# Endpoint for getting all revenue for a specific chip
@app.route("/chips/<int:chip_id>/revenue", methods=["GET"])
def get_revenue(chip_id):
    chip_revenue = [rev for rev in revenue if rev["chip_id"] == chip_id]
    return jsonify({"transistors": chip_revenue})


if __name__ == "__main__":
    app.run(debug=True)


# http://127.0.0.1:5000/chips
# http://127.0.0.1:5000/chips/2
# http://127.0.0.1:5000/chips/2/revenue
