""" The difference here is that we are using a dictionary to hold
the functions that we need to pass to app. Instead of using an interface
(an abstract class).
"""
from dataclasses import dataclass
from typing import Callable

# this is definition 
def app(client_interface: dict[Callable]):
    client_interface["getuser"]("bob@clean.com")
    user = User("Bob", "bob@clean.com")
    client_interface["createuser"](user)

@dataclass
class User:
    name: str
    email: str

def getuser(email: str):
    print(f"Getting user... {email}")
    
def createuser(user: User):
    print(f"Creating user... {user.name}")

client_interface = {
    "getuser": getuser,
    "createuser": createuser,
}

# this is calling
if __name__ == "__main__":
    app(client_interface)