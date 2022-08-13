The `models` directory contains code that acts as the middle ware between the database and the native data structures worlds of Python.

Inside the `models` directory we include classes or functions that deals with the database and transform them into native objects.

For example we can store ODBC and SQL code. Or we can store ORM code. In all these examples we transform information living inside the database into information that lives as a native object.

The functions and classes defined in the `models` directory are used by the functions and classes defined inside the `resources` directory.

And those `resources` functions and classes exchange or execute the internal logic operations that are triggered by external requests.
That is, the `resources` directory contains code that expose the endpoints to the external world and also code that executes what ever is being requested.