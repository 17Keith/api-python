#!flask/bin/python

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    # return "I hope it is working"
    return "it is working"


if __name__ == "__main__":
    app.run(debug=True)
