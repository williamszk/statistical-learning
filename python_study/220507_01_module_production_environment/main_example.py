# ------------------------------------- #
# dev_main.py
TESTING = True
import db_connection
db = db_connection.Database()
# ------------------------------------- #
# prod_main.py
import db_connection
db = db_connection.Database()

# ------------------------------------- #
# db_connection.py
import __main__
# where does __main__ comes from?
# we can have a __main__.py file in the directory

class TestingDatabase(object):
    pass

class RealDatabase(object):
    pass


if __main__.TESTING:
    Database = TestingDatabase
else:
    Database = RealDatabase

# module scoped code, that is not inside any function or method
# how is this related to namespace?
# the module is the file/script itself




