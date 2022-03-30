# https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/5960152#overview

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name):
        return {"student": name}


api.add_resource(Student, "/student/<string:name>")




app.run(port=5000, debug=True)
