from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug import serving

app = Flask(__name__)
api = Api(app)

class TestApi(Resource):
    def post(self):
        # request_data = request.get_json()
        request_data = request.get_data()
        response_body = request_data
        response_header = {"Content-Type": "application/octet-stream"}
        status_code = 200

        response = app.make_response((response_body, status_code, response_header))

        return response


api.add_resource(TestApi, "/")

if __name__ == "__main__":
    serving.run_simple("0.0.0.0", 5000, app)