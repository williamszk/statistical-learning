:: This is a bat file to ease the workflow for deleting and
:: then creating the database and then testing the endpoints

DEL data.db

python create_tables.py

python client_insert_item.py
