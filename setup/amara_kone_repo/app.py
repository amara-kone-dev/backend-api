from flask import Flask, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'dev-key')

@app.route('/')
def index():
    return jsonify({"message": "TechShield API v1.0", "status": "running"})

@app.route('/api/auth/login', methods=['POST'])
def login():
    return jsonify({"error": "Not implemented"}), 501

@app.route('/api/users')
def users():
    return jsonify({"error": "Authentication required"}), 401

@app.route('/api/projects')
def projects():
    return jsonify({"error": "Authentication required"}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5000)
