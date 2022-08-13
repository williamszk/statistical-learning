import sqlite3


def main():
    connection = sqlite3.connect("../db.sqlite")
    cursor = connection.cursor()

    query = """--sql
    SELECT * FROM users;
    """

    for row in cursor.execute(query):
        print(row)

    connection.close()


if __name__ == "__main__":
    main()
