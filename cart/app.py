from flask import Flask, jsonify, request

app = Flask(__name__)
cart = []

@app.route("/cart", methods=["GET"])
def get_cart():
    return jsonify(cart)

@app.route("/cart", methods=["POST"])
def add_to_cart():
    item = request.json.get("item")
    cart.append(item)
    return jsonify({"message": "Item added to cart", "cart": cart})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
