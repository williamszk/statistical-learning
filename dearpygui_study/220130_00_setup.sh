
# create a mysql database inside a container

# CONTAINER ID   IMAGE     COMMAND       CREATED        STATUS                    PORTS     NAMES
# 0267890844bb   ubuntu    "/bin/bash"   23 hours ago   Exited (0) 10 hours ago             webdev_study
# 0a792f11a2a8   ubuntu    "/bin/bash"   6 days ago     Exited (130) 6 days ago             go_study

docker run --name mysql_study_dear -it ubuntu /bin/bash

# inside the container
apt update

# how to install mysql server in ubuntu?
# https://docs.rackspace.com/support/how-to/install-mysql-server-on-the-ubuntu-operating-system/
apt install mysql-server -y


# check if mysql server is running

service --status-all
# root@ba7f51df734d:/# service --status-all
#  [ ? ]  hwclock.sh
#  [ - ]  mysql
#  [ - ]  procps

service mysql status
# root@ba7f51df734d:/# service mysql status
#  * MySQL is stopped.

service mysql start
# root@ba7f51df734d:/# service mysql start
# * Starting MySQL database server mysqld
# su: warning: cannot change directory to /nonexistent: No such file or directory

service mysql status
# root@ba7f51df734d:/# service mysql status
#  * /usr/bin/mysqladmin  Ver 8.0.27-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
# Copyright (c) 2000, 2021, Oracle and/or its affiliates.

# Oracle is a registered trademark of Oracle Corporation and/or its
# affiliates. Other names may be trademarks of their respective
# owners.

# Server version          8.0.27-0ubuntu0.20.04.1
# Protocol version        10
# Connection              Localhost via UNIX socket
# UNIX socket             /var/run/mysqld/mysqld.sock
# Uptime:                 38 sec

# Threads: 2  Questions: 8  Slow queries: 0  Opens: 117  Flush tables: 3  Open tables: 36  Queries per second avg: 0.210



# using mysql shell
cd ~
/usr/bin/mysql -u root -p
# no password
# there is password that we need to enter in installation time
# can we change the password of root later?



# root@ba7f51df734d:~# /usr/bin/mysql -u root -p
# Enter password: 
# Welcome to the MySQL monitor.  Commands end with ; or \g.
# Your MySQL connection id is 12
# Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

# Copyright (c) 2000, 2021, Oracle and/or its affiliates.

# Oracle is a registered trademark of Oracle Corporation and/or its
# affiliates. Other names may be trademarks of their respective
# owners.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# mysql> 

# "If you logged in by entering a blank password, or if you want to change the 
# root password that you set, you can create or change the password."

# given that the mysql server is running inside a container for 
# personal use I'll set a generic password
UPDATE mysql.user SET authentication_string = PASSWORD("pass123") WHERE User = "root";

# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '("pass123") WHERE User = "root"' at line 1
# This function was removed in MySQL 8.0.11
# My mysql is 8.0.27

ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'pass123';
exit;

# mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'pass123';
# Query OK, 0 rows affected (0.15 sec)

# test it:
mysql -u root -p
# enter: pass123
# it works

# root@ba7f51df734d:~# mysql -u root -p
# Enter password: 
# Welcome to the MySQL monitor.  Commands end with ; or \g.
# Your MySQL connection id is 14
# Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

# Copyright (c) 2000, 2021, Oracle and/or its affiliates.

# Oracle is a registered trademark of Oracle Corporation and/or its
# affiliates. Other names may be trademarks of their respective
# owners.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# mysql> 

# There is a difference between "database server" and a "database"
# MySQL is a "database server" it is a software used to interact with the database
# a "database" is another entity, it is a collection of tables, that is usually
# associated with a "database server": MySQL, Postgres, Oracle etc
#

# search for an interesting database or data example in Kaggle
# https://www.kaggle.com/fedesoriano/stellar-classification-dataset-sdss17
# this dataset seems to be interesting

# just for experiment we'll create a database
# (inside the mysql shell in the server)

CREATE DATABASE stellarclassification;
# mysql> CREATE DATABASE stellarclassification;
# Query OK, 1 row affected (0.19 sec)

SHOW DATABASES;
# mysql> SHOW DATABASES;
# +-----------------------+
# | Database              |
# +-----------------------+
# | information_schema    |
# | mysql                 |
# | performance_schema    |
# | stellarclassification |
# | sys                   |
# +-----------------------+
# 5 rows in set (0.01 sec)

# how to delete a database?
DROP DATABASE stellarclassification;
# mysql> DROP DATABASE stellarclassification;
# Query OK, 0 rows affected (0.35 sec)

SHOW DATABASES;
# mysql> SHOW DATABASES;
# +--------------------+
# | Database           |
# +--------------------+
# | information_schema |
# | mysql              |
# | performance_schema |
# | sys                |
# +--------------------+
# 4 rows in set (0.00 sec)
# 
# Note that "stellarclassification" is there anymore

# create again the database
# 
CREATE DATABASE stellar_classification;
SHOW DATABASES;
# mysql> SHOW DATABASES;
# +------------------------+
# | Database               |
# +------------------------+
# | information_schema     |
# | mysql                  |
# | performance_schema     |
# | stellar_classification |
# | sys                    |
# +------------------------+
# 5 rows in set (0.01 sec)


# When applications connect to the database using the root user, they usually have more privileges than they need. 
# You can add users that applications can use to connect to the new database. 
# In the following example, a user named "william" is created.

INSERT INTO mysql.user (User,Host,authentication_string,ssl_cipher,x509_issuer,x509_subject)
    VALUES('william','localhost',PASSWORD('pass123'),'','','');
# This is not working
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL 
# server version for the right syntax to use near '('pass123'),'','','')' at line 2


# https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql

CREATE USER 'william'@'localhost' IDENTIFIED BY 'pass123';
# mysql> CREATE USER 'william'@'localhost' IDENTIFIED BY 'pass123';
# CREATE USER 'william'@'localhost' IDENTIFIED BY 'pass123';


# to see the list of users
SELECT User, Host, authentication_string FROM mysql.user;
# mysql> SELECT User, Host, authentication_string FROM mysql.user;
# +------------------+-----------+------------------------------------------------------------------------+
# | User             | Host      | authentication_string                                                  |
# +------------------+-----------+------------------------------------------------------------------------+
# | debian-sys-maint | localhost | $A$005$?GrJThcfeliB\\J:%WNdNOGfXqWrU9cneiDOKi2kVe1jCUuMnr/t2qDkYrK80 |
# | mysql.infoschema | localhost | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
# | mysql.session    | localhost | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
# | mysql.sys        | localhost | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
# | root             | localhost | $A$005$M"I2x=hKD3O
#                                                    2cBF3d1nVP1YvZa.Yk/7kkqZqMWYg.gRaFOEspLlzmJw4 |
# +------------------+-----------+------------------------------------------------------------------------+
# 5 rows in set (0.00 sec)

# user william is not there

# try again:
CREATE USER 'william'@'localhost' IDENTIFIED BY 'pass123';
GRANT ALL PRIVILEGES ON * . * TO 'william'@'localhost';
FLUSH PRIVILEGES;

SELECT User, Host, authentication_string FROM mysql.user;
# mysql> SELECT User, Host, authentication_string FROM mysql.user;
# +------------------+-----------+------------------------------------------------------------------------+
# | User             | Host      | authentication_string                                                  |
# +------------------+-----------+------------------------------------------------------------------------+
# | debian-sys-maint | localhost | $A$005$?GrJThcfeliB\\J:%WNdNOGfXqWrU9cneiDOKi2kVe1jCUuMnr/t2qDkYrK80 |
# | mysql.infoschema | localhost | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
# | mysql.session    | localhost | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
# | mysql.sys        | localhost | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
# | root             | localhost | $A$005$M"I2x=hKD3O
# | william          | localhost | $A$005$A(-ekc=?kWFY5PG%UOto2I4chwrnqfgkcJOOSLl5POIk8Ek97Oub.shdz8o0 |
# +------------------+-----------+------------------------------------------------------------------------+
# 6 rows in set (0.00 sec)

# now it is appearing...

# GRANT type_of_permission ON database_name.table_name TO 'username'@'localhost';

# type_of_permission can be of the following types:
# ALL PRIVILEGES- as we saw previously, this would allow a MySQL user full access to a designated database (or if no database is selected, global access across the system)
# CREATE- allows them to create new tables or databases
# DROP- allows them to them to delete tables or databases
# DELETE- allows them to delete rows from tables
# INSERT- allows them to insert rows into tables
# SELECT- allows them to use the SELECT command to read through databases
# UPDATE- allow them to update table rows
# GRANT OPTION- allows them to grant or remove other users’ privileges

# given that we want to build a program that can only consume the data from the database
# we should grant only SELECT option for specific databases...

SHOW GRANTS FOR "william"@"localhost";
# mysql> SHOW GRANTS FOR "william"@"localhost";
# +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
# | Grants for william@localhost                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
# +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
# | GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `william`@`localhost`                                                                                                                                                                                                                                                                                                 |
# | GRANT APPLICATION_PASSWORD_ADMIN,AUDIT_ADMIN,AUTHENTICATION_POLICY_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,ENCRYPTION_KEY_ADMIN,FLUSH_OPTIMIZER_COSTS,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,GROUP_REPLICATION_STREAM,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,PASSWORDLESS_USER_ADMIN,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_USER_ID,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,XA_RECOVER_ADMIN ON *.* TO `william`@`localhost` |
# +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+



# GRANT is a command that is part of the Data Control Language

# end of https://docs.rackspace.com/support/how-to/install-mysql-server-on-the-ubuntu-operating-system/


# exit and enter mysql shell using william user
exit;
mysql -u william -p
# root@ba7f51df734d:~# mysql -u william -p
# Enter password: 
# Welcome to the MySQL monitor.  Commands end with ; or \g.
# Your MySQL connection id is 18
# Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

# Copyright (c) 2000, 2021, Oracle and/or its affiliates.

# Oracle is a registered trademark of Oracle Corporation and/or its
# affiliates. Other names may be trademarks of their respective
# owners.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# mysql> 


# create a table inside the database stellar_classification
# table name star classification

# create a program that can create a table in sql using the dearpygui interface
# we just need to pass a csv file
# we need to take care for all elements in each column to have a single type
# 


# how to connect dearpygui with the mysql database?

# if we turn off and then turn of the container
# the mysql service will start automatically?

# william@william-300E5M-300E5L:~/Documents/statistical-learning$ docker ps
# CONTAINER ID   IMAGE     COMMAND       CREATED       STATUS         PORTS     NAMES
# ba7f51df734d   ubuntu    "/bin/bash"   3 hours ago   Up 2 seconds             mysql_study_dear
# william@william-300E5M-300E5L:~/Documents/statistical-learning$ docker exec -it mysql_study_dear /bin/bash
# root@ba7f51df734d:/# service mysql status
#  * MySQL is stopped.
# root@ba7f51df734d:/# 

# No it will not start automatically when the container starts
# How to make the mysql start when the container starts?

# again:
# https://docs.rackspace.com/support/how-to/install-mysql-server-on-the-ubuntu-operating-system/
# let's test with:
service mysql enable
# root@ba7f51df734d:/# service mysql enable
# Usage: /etc/init.d/mysql start|stop|restart|reload|force-reload|status
# it doesn't work

# maybe we can start the service of mysql when we start the container
docker stop mysql_study_dear
docker ps
docker start mysql_study_dear
# this command will start the mysql service inside the container
docker exec mysql_study_dear service mysql start
# william@william-300E5M-300E5L:~/Documents/statistical-learning$ docker exec mysql_study_dear service mysql start
#  * Starting MySQL database server mysqld
# su: warning: cannot change directory to /nonexistent: No such file or directory
#    ...done.
docker exec mysql_study_dear service mysql status
# william@william-300E5M-300E5L:~/Documents/statistical-learning$ docker exec mysql_study_dear service mysql status
#  * /usr/bin/mysqladmin  Ver 8.0.27-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
# Copyright (c) 2000, 2021, Oracle and/or its affiliates.

# Oracle is a registered trademark of Oracle Corporation and/or its
# affiliates. Other names may be trademarks of their respective
# owners.

# Server version          8.0.27-0ubuntu0.20.04.1
# Protocol version        10
# Connection              Localhost via UNIX socket
# UNIX socket             /var/run/mysqld/mysqld.sock
# Uptime:                 51 sec

# Threads: 2  Questions: 8  Slow queries: 0  Opens: 117  Flush tables: 3  Open tables: 36  Queries per second avg: 0.156

# it worked...


# let's try to use python to connect to the mysql in the container

# see ip address of the container
# root@ba7f51df734d:~# ifconfig
# bash: ifconfig: command not found

# apt install net-tools -y
# ifconfig
# 
# root@ba7f51df734d:~# ifconfig
# eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#         inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255
#         ether 02:42:ac:11:00:02  txqueuelen 0  (Ethernet)
#         RX packets 151  bytes 213808 (213.8 KB)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 86  bytes 5860 (5.8 KB)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

# lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
#         inet 127.0.0.1  netmask 255.0.0.0
#         loop  txqueuelen 1000  (Local Loopback)
#         RX packets 0  bytes 0 (0.0 B)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 0  bytes 0 (0.0 B)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0



# https://docs.rackspace.com/support/how-to/install-mysql-server-on-the-ubuntu-operating-system/
# If you have iptables enabled and want to connect to the MySQL database from another machine, 
# you must open a port in your server’s firewall (the default port is 3306). 
# You don’t need to do this if the application that uses MySQL is running on the same server.

docker exec -it mysql_study_dear /bin/bash
cd
ufw
# root@ba7f51df734d:~# ufw
# bash: ufw: command not found
apt install ufw -y
ufw
# root@ba7f51df734d:~# ufw
# ERROR: not enough args
ufw enable

# root@ba7f51df734d:~# ufw enable
# ERROR: problem running ufw-init
# iptables-restore v1.8.4 (legacy): iptables-restore: unable to initialize table 'filter'

# Error occurred at line: 1
# Try `iptables-restore -h' or 'iptables-restore --help' for more information.
# iptables-restore v1.8.4 (legacy): iptables-restore: unable to initialize table 'filter'

# Error occurred at line: 1
# Try `iptables-restore -h' or 'iptables-restore --help' for more information.
# iptables-restore v1.8.4 (legacy): iptables-restore: unable to initialize table 'filter'

# Error occurred at line: 1
# Try `iptables-restore -h' or 'iptables-restore --help' for more information.
# iptables-restore v1.8.4 (legacy): iptables-restore: unable to initialize table 'filter'

# Error occurred at line: 1
# Try `iptables-restore -h' or 'iptables-restore --help' for more information.
# iptables-restore v1.8.4 (legacy): iptables-restore: unable to initialize table 'filter'

# Error occurred at line: 12
# Try `iptables-restore -h' or 'iptables-restore --help' for more information.
# iptables-restore v1.8.4 (legacy): iptables-restore: unable to initialize table 'filter'

# Error occurred at line: 12
# Try `iptables-restore -h' or 'iptables-restore --help' for more information.
# iptables-restore v1.8.4 (legacy): iptables-restore: unable to initialize table 'filter'

# Error occurred at line: 1
# Try `iptables-restore -h' or 'iptables-restore --help' for more information.
# iptables-restore v1.8.4 (legacy): iptables-restore: unable to initialize table 'filter'

# Error occurred at line: 1
# Try `iptables-restore -h' or 'iptables-restore --help' for more information.
# iptables-restore v1.8.4 (legacy): iptables-restore: unable to initialize table 'filter'

# Error occurred at line: 1
# Try `iptables-restore -h' or 'iptables-restore --help' for more information.
# iptables-restore v1.8.4 (legacy): iptables-restore: unable to initialize table 'filter'

# Error occurred at line: 1
# Try `iptables-restore -h' or 'iptables-restore --help' for more information.
# sysctl: setting key "net.ipv4.conf.all.accept_redirects", ignoring: Read-only file system
# sysctl: setting key "net.ipv4.conf.default.accept_redirects", ignoring: Read-only file system
# sysctl: setting key "net.ipv6.conf.all.accept_redirects", ignoring: Read-only file system
# sysctl: setting key "net.ipv6.conf.default.accept_redirects", ignoring: Read-only file system
# sysctl: setting key "net.ipv4.icmp_echo_ignore_broadcasts", ignoring: Read-only file system
# sysctl: setting key "net.ipv4.icmp_ignore_bogus_error_responses", ignoring: Read-only file system
# sysctl: setting key "net.ipv4.icmp_echo_ignore_all", ignoring: Read-only file system
# sysctl: setting key "net.ipv4.conf.all.log_martians", ignoring: Read-only file system
# sysctl: setting key "net.ipv4.conf.default.log_martians", ignoring: Read-only file system

# Problem loading ipv6 (skipping)
# Problem running '/etc/ufw/before.rules'
# Problem running '/etc/ufw/after.rules'
# Problem running '/etc/ufw/user.rules'

ufw allow mysql
# root@ba7f51df734d:~# ufw allow mysql
# WARN: initcaps
# [Errno 2] iptables v1.8.4 (legacy): can't initialize iptables table `filter': Permission denied (you must be root)
# Perhaps iptables or your kernel needs to be upgraded.

# Rules updated
# Rules updated (v6)




# https://askubuntu.com/questions/28215/how-can-i-fix-the-iptables-error-message-unable-to-initialize-table-filter
# iptables-restore v1.8.4 (legacy): iptables-restore: unable to initialize table 'filter'
iptables-restore
# idk does nothing

# https://itectec.com/ubuntu/ubuntu-how-to-fix-the-iptables-error-message-unable-to-initialize-table-filter/
modprobe /lib/modules/$(uname -r)/kernel/net/ipv4/netfilter/iptable_filter.ko
# bash: modprobe: command not found
# idk 


iptables-restore -h
# root@ba7f51df734d:~# iptables-restore -h
# Usage: iptables-restore [-c] [-v] [-V] [-t] [-h] [-n] [-w secs] [-W usecs] [-T table] [-M command] [file]
#            [ --counters ]
#            [ --verbose ]
#            [ --version]
#            [ --test ]
#            [ --help ]
#            [ --noflush ]
#            [ --wait=<seconds>
#            [ --wait-interval=<usecs>
#            [ --table=<TABLE> ]
#            [ --modprobe=<command> ]



# https://www.tutorialworks.com/container-networking/

# https://docs.docker.com/config/containers/container-networking/

# By default, when you create or run a container using docker create or docker run, it does not publish any of its ports to the outside world. 
# To make a port available to services outside of Docker, or to Docker containers which are not connected to the container’s network, use the 
# --publish or -p flag. This creates a firewall rule which maps a container port to a port on the Docker host to the outside world. Here are some examples.

# -p 8080:80	Map TCP port 80 in the container to port 8080 on the Docker host.
# mysql uses port 3306
# Maybe I can expose the docker port 3306 to the host 3306 port

# Can I expose a port of a running container?

# https://stackoverflow.com/a/42071577
# I think I can't...
# 
# I'll build another container then...




