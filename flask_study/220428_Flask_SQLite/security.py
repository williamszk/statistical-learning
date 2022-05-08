from user import User
import sqlite3
import hmac


def authenticate(username, password):

    user = User.find_by_username(username)

    if hmac.compare_digest(user.password, password):
        return user


def identity(payload):

    # this payload is specific from Flask-JWT
    user_id = payload["identity"]

    user = User.find_by_userid(user_id)

    return user

