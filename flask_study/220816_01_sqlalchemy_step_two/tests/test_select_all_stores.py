
def test_main():
    import sqlite3

    connection = sqlite3.connect("../src/db.sqlite")
    cursor = connection.cursor()
    query = """ --sql
    SELECT * FROM stores;
    """

    for row in cursor.execute(query):
        print(row)

    connection.close()

if __name__ == "__main__":
    test_main()