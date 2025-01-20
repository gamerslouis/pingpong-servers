from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    # Print request time to console
    print("Request time:", datetime.now().isoformat())
    # Print all request headers to console
    for header, value in request.headers.items():
        print(f"{header}: {value}")

    return jsonify({"message": "pong"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
