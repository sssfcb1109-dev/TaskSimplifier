#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/reply', methods=['POST'])
def reply():
    data = request.get_json(force=True, silent=True) or {}
    response = {
        'to': data.get('from', ''),
        'subject': f"Re: {data.get('subject', '')}",
        'body': 'Thank you for your message. This is an automated reply.'
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
