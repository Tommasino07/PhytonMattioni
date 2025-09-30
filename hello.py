from flask import Flask


app = Flask(__name__)


@app.route("/getAllDataInHtml")
def hello():
    return "Hello, World!"