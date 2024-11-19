IN THIS GIT REPO WE ARE TRYING TO BUILD A 3-TIRE ARCHITECTURE FOR A PYTHON FLASK APPLICATION: 
* FOR THIS WE HAVE USED DOCKER-COMPOSE TO LAUNCH THE TEST ENVIRONMENT.
* THE NGINX SERVER IS DEPLOYED MANUALLY IN ANOTHER INSTACE AND INSTRUMENTED WITH OPENTELEMETRY, THE NGINX VERSION USED IS 1.26.0 AND THE OPENTELEMETRY VERSION IS 1.26.0 WHICH IS TAKEN FROM THE GITHUB LINK: https://github.com/open-telemetry/opentelemetry-cpp-contrib/releases
THE RELEASE VERISION IS webserver/v1.1.0.
* FOR THE INSTRUMENTATION OF OPENTELEMETRY WE FOLLOWED THE STEPS FROM : https://opentelemetry.io/blog/2022/instrument-nginx/

* IN THIS CODE WE ARE TRYING TO SIMULATE A 3-TIRE ARCHITECTURE WHERE THE PAYMENT SERVICE WILL NOT BE INSTRUMENTED WITH OPENTELEMETRY AND ALL THE REMAINING SERVICES ARE INSTRUMENTED WITH OPENTELEMETRY. AND TRIED TO OBSERVE THE SPANS WHEN A NON INSTRUMENTED SEVICE IS TRIGGERED FROM NGINX INSTRUMENTED SERVICE.
* WE ARE TRYING TO TRIGGER A INSTRUMENTED SERVICE FROM A NON-INSTRUMENTED SERVICE.
  
**NGINX SETUP**

* WE HAVE TAKEN AN EC2 UBUNTU INSTANCE WHERE WE HAVE INSTALLED THE NGINX V 1.26.0 , THE OPENTELEMETRY .TAR FILE IS TAKEN FROM THE OPENSOURCE GIT HUB LINK : https://github.com/open-telemetry/opentelemetry-cpp-contrib/releases
* NOW SSH INTO YOUR MACHINE AND GO TO /opt DIRECTORY AND DOWNLOAD THE .TAR FILE AND UNTAR THE FILE.
* THE /opt/opentelemetry-sdk DIRECTORY RUN ./INSTALL.SH FILE. THEN ADDED THE PATH FOR THE LIBRARIES IN THE /etc/environments : LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/opentelemetry-webserver-sdk/sdk_lib/lib
* NOW NAVIGATE TO /OPT/OPENTELEMETRY-SDK/WEBSERVER/NGINX/1.26.0/ngx_http_opentelemetry_module.so COPY IT AND PAST IT IN THE /etc/nginx/modules/ngx_http_opentelemetry_module.so AND GIVE THE READ AND EXECUTE PERMISSIONS FOR THE FILE AND MODULE DIRECTORY FOR ALL USERS.
* NOW CONFIGURE THE nginx.conf FILE WITH THE DETAILS PROVIDED IN THE NGINX FOLDER IN GIT REPOSITORY.
* ALSO CONFIGURE THE /etc/nginx/cong.d/opentememetry.conf  WITH THE CONTENTES PRESENT GIVEN IN THE NGINX FOLDER IN THE GIT REPO.
* AFTER DOING THE FOLLOWING CHANGES RELOAD THE DAEMON SERVICE AND RESTART THE NGINX SERVICE.

 **LAUNCHING THE SERVICES DOCKER-COMPOSE** 

 * CLONE THIS REPO AND GIVE THE APPROPRIATE IP ADDRESSES FOR THE OTEL-COLLECTOR INSTANCE IF YOU ARE RUNNING SAPERATELY.
 * AFTER THIS CD TO THE LOCATION WHERE THE DOCKER-COMPOSE.YAML FILE IS PRESENT AND RUN `docker-compose up -d`
 * THIS COMMAND WILL LAUNCH THE DOCKER CONTAINER OF THE SERVICES I.E, ITEMS,CART,DB,PAYMENT
 * TO CHECK WHETHER THE SERVICES ARE RUNNING RUN COMMAND `docker ps or docker container ls  `. USE SHOULD BE ABLE TO VIEW THE RUNNING CONTAINERS WITH THE EXPOSED PORTS.

**TESTING**
* NOW OPEN ANY WEBBROWSER AND RAISE A HTTP REQUEST `http://<ip-of-nginx>/items` THIS SHOULD GIVE THE SUCCESS RESPONSE AND `http://<ip-of -nginx>/items?id=1` THIS SHOULD GIVE YOU THE ERROR RESPONSE.
----
  **OPENTELEMETRY VERSIONS INSTALLED**

opentelemetry-api                        1.28.1
opentelemetry-distro                     0.49b1
opentelemetry-exporter-otlp              1.28.1
opentelemetry-exporter-otlp-proto-common 1.28.1
opentelemetry-exporter-otlp-proto-grpc   1.28.1
opentelemetry-exporter-otlp-proto-http   1.28.1
opentelemetry-instrumentation            0.49b1
opentelemetry-instrumentation-asyncio    0.49b1
opentelemetry-instrumentation-dbapi      0.49b1
opentelemetry-instrumentation-flask      0.49b1
opentelemetry-instrumentation-grpc       0.49b1
opentelemetry-instrumentation-jinja2     0.49b1
opentelemetry-instrumentation-logging    0.49b1
opentelemetry-instrumentation-mysql      0.49b1
opentelemetry-instrumentation-requests   0.49b1
opentelemetry-instrumentation-sqlite3    0.49b1
opentelemetry-instrumentation-threading  0.49b1
opentelemetry-instrumentation-urllib     0.49b1
opentelemetry-instrumentation-urllib3    0.49b1
opentelemetry-instrumentation-wsgi       0.49b1
opentelemetry-proto                      1.28.1
opentelemetry-sdk                        1.28.1
opentelemetry-semantic-conventions       0.49b1
opentelemetry-util-http                  0.49b1
