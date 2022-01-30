# pip3 install mysql-connector-python
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

# python3
import mysql.connector

connection = mysql.connector.connect(
                            user='william', 
                            password='pass123',
                            host='127.0.0.1',
                            database='stellar_classification')

# from inside the same container as the database I can connect with
# mysql...
# the problem is to expose the container to connections from the host or other containers


connection.close()

# ModuleNotFoundError: No module named 'mysql'
# pip3 install mysql-connector

# see ip address of the container
# apt install net-tools -y
# ifconfig
# 

# I had a problem with connection refused with the database
# mysql.connector.errors.InterfaceError: 2003: Can't connect to MySQL server on '172.17.0.2:3306' (111 Connection refused)
# maybe there is something that I need to configure in the databse


# mysql.connector.errors.InterfaceError: 2013: Lost connection to MySQL server during query