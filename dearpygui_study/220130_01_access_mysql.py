# pip3 install pyodbc

# python3
import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
server = 'localhost,3306' # to specify an alternate port
# server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'william' 
password = 'pass123' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# problem installing pyodbc
# 56 | #include <sql.h>
# https://github.com/mkleehammer/pyodbc/issues/441
# sudo apt install unixodbc-dev









