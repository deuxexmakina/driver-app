# api.py
from flask import request, jsonify

def init_app(app):
    @app.route('/', methods=['GET'])
    def get():
        return jsonify({'msg': 'Hello, World!'}), 200

