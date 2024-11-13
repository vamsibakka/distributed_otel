FROM python:3.9-slim

WORKDIR /app

RUN pip install --upgrade pip
COPY . /app
RUN pip install -r requirements.txt

# OpenTelemetry environment variables for zero-code instrumentation
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://3.86.240.124:4317"
ENV OTEL_SERVICE_NAME="cart"  

EXPOSE 5002  

CMD ["opentelemetry-instrument", "python", "app.py"]
