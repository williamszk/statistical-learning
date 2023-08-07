from flask import Flask

application = app = Flask(__name__)


@application.route("/")
def hello():
    return "Hello, Elastic Beanstalk! This is using docker..."


if __name__ == "__main__":
    application.run(host="0.0.0.0")
