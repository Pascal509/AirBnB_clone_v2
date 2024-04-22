#!/usr/bin/python3
"""
This script starts a Flask web application with specified routes.
Each route uses `strict_slashes=False` to allow access with or
without a trailing slash.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' at the root URL path. """
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' at the '/hbnb' URL path. """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
