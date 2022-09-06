from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from security import authenticate, identity

from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# To allow flask propagating exception even if debug is set to false on app
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'mysecretkey'
db.init_app(app)
api = Api(app)


# with this functionwe don't need to create the tables
# in another script
@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')




if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
