from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def get_hi():
    return jsonify({"message": "Hi!"})


if __name__ == "__main__":
    app.run(hots="0.0.0.0")
