from flask import Flask

application = app = Flask(__name__)


@application.route("/")
def hello():
    return "Hello, Elastic Beanstalk! This is using docker..; this is now building from the docker-compose file and not downloading from dockerhub"


if __name__ == "__main__":
    application.run(host="0.0.0.0")
