# https://www.youtube.com/watch?v=sZszl8HO2RE&ab_channel=Linode

apt update
apt upgrade -y

# install SAR system activity reporter
# sysstat
# the package that contains the sar command
apt install sysstat -y
# usually it is already installed

# we need to change the config file from sysstat
vim /etc/default/sysstat

cat /etc/cron.d/sysstat
# # The first element of the path is a directory where the debian-sa1
# # script is located
# PATH=/usr/lib/sysstat:/usr/sbin:/usr/sbin:/usr/bin:/sbin:/bin

# # Activity reports every 10 minutes everyday
# 5-55/10 * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1 1

# # Additional run at 23:59 to rotate the statistics file
# 59 23 * * * root command -v debian-sa1 > /dev/null && debian-sa1 60 2

# here is where the logs are stored
# they are run every 10 minutes, we can change that
ls -l /var/log/sysstat



sar -b

sar -b
















