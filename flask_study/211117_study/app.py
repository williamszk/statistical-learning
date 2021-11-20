from flask import Flask
# classes in Python start with a Upper case letters
# they are Pascal case
# packages are always in lower case usually one word
# 
# hello world!

app = Flask(__name__)
# at run time __name__ give each file a unique name

@app.route("/") # define the end point
def home():
    return "Hello World!"

app.run(port=5000)

