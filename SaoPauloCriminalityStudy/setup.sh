
# Those are some setup notes about 
# using nginx to serve the .html

apt update


service nginx status

apt install nginx -y

nginx -v

# (.venv) root@17bd5980aa2c:~/statistical-learning# nginx -v
# nginx version: nginx/1.18.0 (Ubuntu)

service nginx status

# the container private ip address
# "IPAddress": "172.17.0.2",
# I used 
# docker inspect <docker container name>

service nginx start

service nginx status

# found that there is also apache running in the same machine
service --status-all

service apache2 stop

service nginx stop

# the html needs to be at the var/www/

# root@17bd5980aa2c:/var/www/html# ls
# index.html  index.nginx-debian.html  info.php

http://172.17.0.2/index.html
http://172.17.0.2/index.nginx-debian.html
http://172.17.0.2/html/info.php





