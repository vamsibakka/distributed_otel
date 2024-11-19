from flask import Flask, jsonify, request
import requests
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry import trace

app = Flask(__name__)

# Instrument Flask and Requests for tracing
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

# Initialize tracer
tracer = trace.get_tracer(__name__)

cart = []

@app.route("/cart", methods=["GET"])
def add_to_cart():
    with tracer.start_as_current_span("add_to_cart"):
        item_id = request.args.get("item_id")
        item_name = request.args.get("name")
        item_price = request.args.get("price")

        if not item_id or not item_name or not item_price:
            return jsonify({"error": "Invalid item details"}), 400

        item = {"id": item_id, "name": item_name, "price": item_price}
        cart.append(item)
        return jsonify({"message": "Item added to cart", "cart": cart})

@app.route("/checkout", methods=["GET"])
def checkout():
    with tracer.start_as_current_span("checkout"):
        # Simulate checkout processing
        query_string = request.query_string.decode()  # Gets the query string part of the request
        # Build the URL for payment service with the query string
        payment_url = f"http://payment-service:5003/payment?{query_string}"
        response = requests.get(payment_url)
        if response.status_code != 200:
            return jsonify({"error": "Payment service failed"}), 500

        return jsonify({"message": "Checkout completed", "payment_details": response.json()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
