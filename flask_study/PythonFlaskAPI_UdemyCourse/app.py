from flask import Flask, jsonify, request, render_template
from itsdangerous import json

app = Flask(__name__)

stores = [
    {
        "name": "My LOTR Store",
        "items": [
            {
                "name": "The One Ring",
                "price": 17.99
            }
        ]
    }
]

@app.route("/")
def home():
    return render_template("index.html")
    # flask will look at the templates folder


@app.route("/lotr")
def get_lotr():
    request_data = request.get_json()
    return jsonify(request_data)


@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name :
            return jsonify(store)
    return jsonify({"Error": "Store not found"})


@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})


@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"Error": "Store not found"})


@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items":store["items"]})
    return jsonify({"Error": "Store not found"})


app.run(port=5000)
# to run just write: python app.py