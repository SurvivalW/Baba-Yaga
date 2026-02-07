from flask import Flask, jsonify, request
from flask_cors import CORS
from collections import OrderedDict

app = Flask(__name__)
CORS(app)

MOCK_PRODUCTS = [
    {
        "id": 1,
        "item": "Milk",
        "store": "Kroger",
        "price": 3.49,
        "stock": 12
    },
    {
        "id": 2,
        "item": "Milk",
        "store": "Walmart",
        "price": 3.19,
        "stock": 20
    },
    {
        "id": 3,
        "item": "Bread",
        "store": "Target",
        "price": 2.29,
        "stock": 8
    }
]

@app.route("/api/search")
def search():
    query = request.args.get("q", "").lower()

    results = [
        p for p in MOCK_PRODUCTS
        if query == p["item"].lower()
    ]

    return jsonify(results)

# TODO: make methods that show results based on proximity to location and price

@app.route("/api/search_lowest")
def search_lowest():
    query = request.args.get("q", "").lower()
    
    results = [
        p for p in MOCK_PRODUCTS
        if query == p["item"].lower()
    ]
    
    sorted_products = sorted(results, key=lambda x: (x["price"], -x["stock"]))
    return jsonify(sorted_products)

if __name__ == "__main__":
    app.run(debug=True)
