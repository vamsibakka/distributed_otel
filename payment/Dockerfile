FROM python:3.9-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY . /app
RUN pip install -r requirements.txt
    #opentelemetry-bootstrap -a install

# OpenTelemetry environment variables for zero-code instrumentation
#ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://ip-address-otel-collector:4317"
#ENV OTEL_SERVICE_NAME="payment"
EXPOSE 5003

CMD ["python", "app.py"]
