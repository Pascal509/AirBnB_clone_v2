#!/usr/bin/python3
"""
Write a script that starts a Flask web application, listening
on 0.0.0.0 port 5000 at different routes with the option
strict_slashes=False in your route definition
"""
# from markupsafe import escape
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' at the root '/' URL path"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' at the '/hbnb' URL path. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Displays C followed by the value of the text variable"""
    # return f"C, {escape(text)}"
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
