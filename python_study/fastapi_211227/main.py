from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# this is what is called an endpoint
# the browser sends a request to this address then the server will respond 
# by sending the requested information or executing the instructions
@app.get("/") # "path operation decorator", "get" = operationr, "/" = path
def index() -> dict[dict[str:str]]:  # "path operation function"
    # return "hey!"
    return {
        "data": {
            "name": "William",
            "amore": "Mie"

        }
    }

@app.get("/about")
def about():
    return {"data": {"content":"about page"}}

# /blog?limit=10&published=true
@app.get("/blog")
# type hinting in FastAPI have concrete effect on the URL query
def blog(limit=10, published: bool = True, type:str="romance", sort: Optional[str] = None):
    if published:
        return {"data": f"My enormous quantity of data; limit of {limit} blogs showing that were published."}
    else:
        return {"data": f"My enormous quantity of data; limit of {limit} blogs showing that were NOT published."}

@app.get("/blog/unpublished")
def unpublished():
    return {"data":"all unpublished blogs"}

# https://youtu.be/7t2alSnE2-I?t=2157

@app.get("/blog/{id}")
def show(id: int):
    return {"data":id}

@app.get("/blog/{id}/comments")
def show(id: int, limit: int = 10): # <==== only accepts id: int
    # return {"data":{id:[{"comments_1":"hello there"}]}}
    return {"data":id, "limit":limit}

# https://youtu.be/7t2alSnE2-I?t=3358



# cd fastapi_211227
# python -m uvicorn main:app --reload
# python -m uvicorn --version
#

# to use the swagger ui 
# localhost:8000/docs