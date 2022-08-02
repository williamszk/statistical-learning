from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from user import UserRegister
from resources.item import Item, ItemList
from security import authenticate, identity

app = Flask(__name__)
# To allow flask propagating exception even if debug is set to false on app
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'mysecretkey'
api = Api(app)

jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
