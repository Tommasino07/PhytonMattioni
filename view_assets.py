import os
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')

@app.route('/images')
def list_images():
    images = []
    for root, dirs, files in os.walk(ASSETS_DIR):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                rel_dir = os.path.relpath(root, ASSETS_DIR)
                rel_file = os.path.join(rel_dir, file) if rel_dir != '.' else file
                images.append(f"/assets/{rel_file}")
    return jsonify(images)

@app.route('/assets/<path:filename>')
def serve_image(filename):
    return send_from_directory(ASSETS_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
