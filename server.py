# server.py
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/run_main', methods=['GET'])
def run_main():
    result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
    return jsonify(result.stdout)

if __name__ == '__main__':
    app.run(debug=True,port=3000)
