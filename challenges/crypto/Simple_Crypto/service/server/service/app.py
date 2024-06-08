from flask import Flask, request, jsonify
from encryption import encrypt, decrypt
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return "Welcome to the Simple Crypto"

@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.json
        message = data.get('message')
        if "Key to GET Flag" == message:
            key_path = os.path.join(os.path.dirname(__file__), 'key.txt')
            with open(key_path, 'r') as key_file:
                key_content = key_file.read().strip()
            encrypted_message = encrypt(key_content)
            return jsonify({"encrypted_message": encrypted_message})
        else:
            encrypted_message = encrypt(message)
            return jsonify({"encrypted_message": encrypted_message})
    except Exception as e:
        logging.error(f"Error in send_message: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/receive', methods=['POST'])
def receive_message():
    try:
        data = request.json
        message = data.get('message')

        key_path = os.path.join(os.path.dirname(__file__), 'key.txt')
        with open(key_path, 'r') as key_file:
            key_content = key_file.read().strip()

        if message == key_content:
            flag_path = os.path.join(os.path.dirname(__file__), 'flag.txt')
            with open(flag_path, 'r') as flag_file:
                flag_content = flag_file.read().strip()
            return jsonify({"message": flag_content})
        else:
            return jsonify({"message": "Message received"})
    except Exception as e:
        logging.error(f"Error in receive_message: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
