def test_main():
    import sqlite3

    connection = sqlite3.connect("../db2.sqlite")
    # sqlite stores all data in a local file
    # sqlite is slower to write

    cursor = connection.cursor()

    create_table = """
    --sql
    CREATE TABLE users (
        id int,
        username text,
        password text
    );
    """

    cursor.execute(create_table)

    # Insert 1 user into the database
    user = (1, "bob", "asdf")
    insert_query = """
    --sql
    INSERT INTO users VALUES (?,?,?);
    """
    cursor.execute(insert_query, user)

    # Insert many users into the database
    users = [
        (2, "alice", "1234"), 
        (3, "eve", "4321")]
    cursor.executemany(insert_query, users)

    # Show users table
    select_query = """
    --sql
    SELECT * FROM users;
    """
    for row in cursor.execute(select_query):
        print(row)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    test_main()