from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    # Use Flask logger to print request time to console
    app.logger.info(f"Request time: {datetime.now().isoformat()}")
    # Use Flask logger to print all request headers to console
    for header, value in request.headers.items():
        app.logger.info(f"Header {header}: {value}")

    return jsonify({"message": "pong"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
