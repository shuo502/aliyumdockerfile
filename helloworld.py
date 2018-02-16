from flask import Flask
from applik import *
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello OpenShift World!"

if __name__ == "__main__":
    app.run()