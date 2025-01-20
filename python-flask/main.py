from flask import Flask, jsonify, request
from datetime import datetime
from logging.config import dictConfig

app = Flask(__name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

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
