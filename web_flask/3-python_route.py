#!/usr/bin/python3
"""A python script that starts a Flask Web App and adds few tweaks
"""

from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnh():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    return f'C {escape(text)}'.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    if text:
        return f'Python {escape(text)}'.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
