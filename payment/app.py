from flask import Flask, jsonify, request
import requests
import time

app = Flask(__name__)

@app.route("/payment", methods=["GET"])
def make_payment():
    # Get query parameters
    query_param = request.args

    # Error scenario: if any query parameters are present (e.g., id=1)
    if "id" in query_param:
        # Simulate delay for testing purposes
        time.sleep(20)  # Simulate a long processing delay
        return jsonify({"error": "Payment failed due to invalid input"}), 500

    # Success scenario: no query parameters
    # Simulate payment processing
    time.sleep(5)

    # Trigger the notification service
    # try:
    #     response = requests.get("http://notification-service:5004/notify")
    #     if response.status_code != 200:
    #         return jsonify({"error": "Notification failed"}), 500
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

    # Return success response
    return jsonify({"status": "success", "transaction_id": "txn_12345"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
