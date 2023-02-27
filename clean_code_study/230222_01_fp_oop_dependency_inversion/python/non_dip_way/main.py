from dataclasses import dataclass

# this is definition 
def app():
    httpclient = HttpClient()
    httpclient.getuser("bob@clean.com")
    user = User("Bob", "bob@clean.com")
    httpclient.createuser(user)

@dataclass
class User:
    name: str
    email: str

@dataclass
class HttpClient:
    def getuser(self, email: str):
        print(f"Getting user... {email}")
    
    def createuser(self, user: User):
        print(f"Creating user... {user.name}")

# this is calling
if __name__ == "__main__":
    app()