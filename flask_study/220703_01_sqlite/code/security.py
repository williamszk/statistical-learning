from hmac import compare_digest
from user import find_by_id, find_by_username


def authenticate(username, password):
    user = find_by_username(username)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return find_by_id(user_id)
