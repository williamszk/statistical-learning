# We use this in the case where we need to spin a jenkins container
# but installing php and composer

FROM jenkins/jenkins

USER root
RUN sudo apt update && apt upgrade -y && reboot \
    apt -y install lsb-release apt-transport-https ca-certificates \
    wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg \
    echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/php.list

RUN apt update \
    apt install php7.4 \
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"




