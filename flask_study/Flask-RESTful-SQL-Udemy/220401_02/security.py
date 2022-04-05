from werkzeug.security import safe_str_cmp # a bit safe way to compare strings, this was relevant for 2.x python
from user import User

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload["identity"]
    return User.find_by_id(user_id)

