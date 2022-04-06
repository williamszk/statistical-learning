# https://stackoverflow.com/q/41149409/8782077

import os

from flask import Flask
import flask_restful


app = Flask(__name__)
api = flask_restful.Api(app)


class APIException(Exception):
    def __init__(self, code, message):
        self._code = code
        self._message = message

    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self._message

    def __str__(self):
        return self.__class__.__name__ + ': ' + self.message


class ResourceDoesNotExist(APIException):
    """Custom exception when resource is not found."""
    def __init__(self, model_name, id):
        message = 'Resource {} {} not found'.format(model_name.title(), id)
        super(Exception, self).__init__(404, message)


class MyResource(flask_restful.Resource):
    def get(self):
        try:
            model = "id of the model"
            if not model:
               raise Exception
        except APIException as e:
            os.abort(e.code, str(e))


api.add_resource(MyResource, "/")


app.run(port=5000, debug=True)

# fail
