:: Deletes the data.db sqlite database and then
:: it creates the users table

DEL data.db

python create_tables.py