from user import User
import sqlite3
import hmac




users = [
    User(1,"bob", "asdf")
]

username_mapping = {getattr(x, "username"): x for x in users}

userid_mapping = {getattr(x, "id"): x for x in users}


def authenticate(username, password):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    query = """
        SELECT * FROM users WHERE username=?;
        """

    user_data = next(cursor.execute(query, (username,)), None)

    connection.close() 

    if user_data:
        user = User(*user_data)

        if hmac.compare_digest(user.password, password):
            return user


def identity(payload): 
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    # this payload is specific from Flask-JWT 
    user_id = payload["identity"]

    query = """
        SELECT * FROM users WHERE id=?;
        """
    
    user_data = next(cursor.execute(query, (user_id,)), None)

    connection.close() 

    if user_data:
        user = User(user_data)

        return user

