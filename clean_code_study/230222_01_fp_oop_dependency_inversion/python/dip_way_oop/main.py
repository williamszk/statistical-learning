""" In here we create an interface (an abstract class) to be passed to app 
in definition phase. The concrete implementation will be known on the calling
phase. app will only know which concrete implementation to call depending on the
concrete class that is instantiated.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str

@dataclass
class ClientInterface(ABC):
    @abstractmethod
    def getuser(self, email:str):
        pass
    
    @abstractmethod
    def createuser(self, user: User):
        pass

@dataclass
class HttpClient(ClientInterface):
    def getuser(self, email: str):
        print(f"Getting user... {email}")
    
    def createuser(self, user: User):
        print(f"Creating user... {user.name}")

# this is definition 
def app(httpclient: ClientInterface):
    httpclient.getuser("bob@clean.com")
    user = User("Bob", "bob@clean.com")
    httpclient.createuser(user)

# this is calling
if __name__ == "__main__":
    httpclient = HttpClient()
    app(httpclient)