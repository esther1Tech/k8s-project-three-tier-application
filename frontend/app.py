from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
import secrets
import requests

app = Flask(__name__)

# Allow frontend to communicate with Flask only
CORS(app, resources={r"/*": {"origins": os.getenv("FRONTEND_URL", "http://localhost:3000")}})

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['BACKEND_URL'] = os.getenv('BACKEND_URL', 'http://localhost:5000')

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/healthz', methods=['GET'])
def healthz():
    return 'Healthy', 200

@app.route('/items', methods=['GET'])
def get_items():
    """Fetch items from backend and send to frontend."""
    backend_url = app.config['BACKEND_URL']
    try:
        response = requests.get(f'{backend_url}/api/items', timeout=5)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Backend service unreachable", "details": str(e)}), 502

@app.route('/save-item', methods=['POST'])
def save_item():
    """Send new item to backend."""
    item_name = request.json.get('name')
    backend_url = app.config['BACKEND_URL']

    if not item_name:
        return jsonify({"error": "Item name is required"}), 400

    try:
        response = requests.post(f'{backend_url}/api/items', json={'name': item_name}, timeout=5)
        response.raise_for_status()
        return jsonify({"message": "Item saved successfully"}), 201
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to save item", "details": str(e)}), 502

@app.route('/delete-item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete item from backend."""
    backend_url = app.config['BACKEND_URL']

    try:
        response = requests.delete(f'{backend_url}/api/items/{item_id}', timeout=5)
        response.raise_for_status()
        return jsonify({"message": "Item deleted successfully"}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to delete item", "details": str(e)}), 502

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
