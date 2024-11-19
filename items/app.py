from flask import Flask, jsonify, request
import requests
import mysql.connector
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry import trace

app = Flask(__name__)

# Instrument Flask and Requests for tracing
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

# Database connection settings
db_config = {
    "host": "mysql-db",
    "user": "root",
    "password": "password",
    "database": "shop"
}

# Initialize tracer
tracer = trace.get_tracer(__name__)

@app.route("/items", methods=["GET"])
def get_items():
    with tracer.start_as_current_span("get_items"):
        # capture the query string from request to /items
        query_string = request.query_string.decode() #Get query string part
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM items")
        items = [{"id": item[0], "name": item[1], "price": item[2]} for item in cursor.fetchall()]
        cursor.close()
        connection.close()

        if not items:
            return jsonify({"error": "No items found"}), 404

        # Automatically trigger add-to-cart for the first item
        item = items[0]
        add_to_cart_response = requests.get(
            f"http://cart-service:5002/cart?item_id={item['id']}&name={item['name']}&price={item['price']}"
        )

        if add_to_cart_response.status_code != 200:
            return jsonify({"error": "Failed to add item to cart"}), 500

        # Trigger checkout
        checkout_response = requests.get(f"http://cart-service:5002/checkout?{query_string}")
        if checkout_response.status_code != 200:
            return jsonify({"error": "Checkout failed"}), 500

        return jsonify({"message": "Order processed successfully", "details": checkout_response.json()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
