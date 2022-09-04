FROM ubuntu:18.04

# Install dependencies
RUN apt update && apt install apache2 -y

# Install apache and run hello world message
RUN echo "Hello World!" > /var/www/html/index.html

# Configure Apache
RUN echo ". /etc/apache2/envvars" > /root/run_apache.sh && \
    echo "mkdir -p /var/run/apache2" >> /root/run_apache.sh && \
    echo "mkdir -p /var/lock/apache2" >> /root/run_apache.sh && \
    echo "/usr/sbin/apache2 -D FOREGROUND" >> /root/run_apache.sh && \
    chmod 755 /root/run_apache.sh

EXPOSE 80

CMD /root/run_apache.sh