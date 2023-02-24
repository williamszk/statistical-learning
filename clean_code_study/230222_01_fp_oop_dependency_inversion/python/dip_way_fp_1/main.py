""" In here we are passing the concrete implementations to app passing
directly the functions as arguments to app.
"""
from dataclasses import dataclass
from typing import Callable

# this is definition 
def app(getuser: Callable, createuser: Callable):
    getuser("bob@clean.com")
    user = User("Bob", "bob@clean.com")
    createuser(user)

@dataclass
class User:
    name: str
    email: str

def getuser(email: str):
    print(f"Getting user... {email}")
    
def createuser(user: User):
    print(f"Creating user... {user.name}")

# this is calling
if __name__ == "__main__":
    app(getuser, createuser)