from flask import Flask, jsonify
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
tracer = trace.get_tracer(__name__)

@app.route("/notify", methods=["GET"])
def notify():
    with tracer.start_as_current_span("notify_payment_completion"):
        # Log a notification message
        print("Notification: Payment completed successfully!")
        return jsonify({"message": "Notification sent"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
