FROM nginx:1.21

#Install the OpenTelemetry NGINX module
RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget https://github.com/nginxinc/nginx-otel/archive/refs/tags/v0.1.1.zip && \
    unzip v0.1.1.zip -d /usr/lib/nginx/modules/ && \
    rm v0.1.1.zip && \
    apt-get remove -y wget unzip && \
    apt-get autoremove -y && \
    apt-get clean

# Copy NGINX configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
