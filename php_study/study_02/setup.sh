
# https://linuxize.com/post/how-to-install-php-on-ubuntu-20-04/

apt update

apt install php libapache2-mod-php -y

service apache2 status
# root@17bd5980aa2c:~/statistical-learning/php_study# service apache2 status
#  * apache2 is not running
service apache2 start
# root@17bd5980aa2c:~/statistical-learning/php_study# service apache2 start
#  * Starting Apache httpd web server apache2                                                                                                                                               AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
#  * 
service apache2 status
# root@17bd5980aa2c:~/statistical-learning/php_study# service apache2 status
#  * apache2 is running

cd /var/www/html
# root@17bd5980aa2c:/var/www/html# ls
# index.html

# find private IP address of container?
# https://www.freecodecamp.org/news/how-to-get-a-docker-container-ip-address-explained-with-examples/

# https://www.google.com/search?q=linux+private+ip+address&oq=linux+private+ip+address&aqs=chrome.0.0i512j0i22i30l3j0i10i22i30j0i22i30l4.4954j0j4&sourceid=chrome&ie=UTF-8
# ifconfig -a. ip addr (ip a) hostname -I | awk '{print $1}'
ifconfig
# 172.17.0.2

# enter this into the browser to access the index.html inside the container
# http://172.17.0.2/index.html

# root@17bd5980aa2c:/var/www/html# cat info.php
# <?php

# phpinfo();

# root@17bd5980aa2c:/var/www/html# 

# enter this in the browser to access the php file
# http://172.17.0.2/info.php

# PHP Version 7.4.3


# to start a server using php
php -S localhost:4000

cd /root/statistical-learning/php_study/study_02
php -S localhost:4000

# root@17bd5980aa2c:~/statistical-learning/php_study/study_02# php -S localhost:4000
# [Sun Mar  6 22:46:54 2022] PHP 7.4.3 Development Server (http://localhost:4000) started
# [Sun Mar  6 22:46:57 2022] 127.0.0.1:46880 Accepted
# [Sun Mar  6 22:46:58 2022] 127.0.0.1:46882 Accepted
# [Sun Mar  6 22:46:58 2022] 127.0.0.1:46882 [404]: (null) / - No such file or directory
# [Sun Mar  6 22:46:58 2022] 127.0.0.1:46882 Closing
# [Sun Mar  6 22:46:58 2022] 127.0.0.1:46880 [404]: (null) /favicon.ico - No such file or directory
# [Sun Mar  6 22:46:58 2022] 127.0.0.1:46880 Closing
















