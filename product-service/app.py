from flask import Flask, request, jsonify

app = Flask(__name__)
products = []

@app.route("/add-product", methods=["POST"])
def add_product():
    data = request.get_json()
    products.append(data)
    return jsonify({"message": "Product added!", "product": data}), 201

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
