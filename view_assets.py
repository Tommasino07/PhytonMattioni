import os
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
