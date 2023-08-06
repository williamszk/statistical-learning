from flask import Flask

application = app = Flask(__name__)


@application.route("/")
def hello():
    return "Hello, Elastic Beanstalk!"


if __name__ == "__main__":
    application.run()
