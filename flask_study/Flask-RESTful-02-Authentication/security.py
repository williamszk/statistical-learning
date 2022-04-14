from user import User

users = [
    User(1,"bob", "asdf")
]

username_mapping = {getattr(x, "username"): x for x in users}

userid_mapping = {getattr(x, "id"): x for x in users}


def authenticate(username, password):
    user = username_mapping.get(username)
    if user and user.password == password:
        return user


def identity(payload): # this is specific from flask_jwt
    user_id = payload["identity"]
    return userid_mapping.get(user_id)