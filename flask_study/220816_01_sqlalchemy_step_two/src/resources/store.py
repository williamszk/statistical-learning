
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #     'name',
    #     type=str,
    #     required=True,
    #     help="This field cannot be left blank.")

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {"message": "Store not found"}, 404

    @jwt_required()
    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': f"An store with name '{name}' already exists."}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
            return store.json(), 200
        except Exception as e:
            print(e)
            return {
                "message": "Something went wrong with the server while inserting the new store"}, 500

    @jwt_required()
    def delete(self, name):
        item = StoreModel.find_by_name(name)
        if item is None:
            return {
                "message": f"Store with name '{name}' does not exist. We can't delete it."}, 400

        item.delete_from_db()
        return {"message": f"Store '{name}' deleted"}


class StoreList(Resource):
    @jwt_required()
    def get(self):
        stores = StoreModel.get_all()
        return {"stores": [x.json() for x in stores]}

