#!/usr/bin/python3
"""
This script starts a Flask web application that listens on
0.0.0.0, port 5000.It includes routes that display text and
HTML based on the URL path.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display 'Hello HBNB!' at the root '/' URL path. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display 'HBNB' at the '/hbnb' URL path. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C ', followed by the value of the text variable,
    underscores replaced with spaces.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Display 'Python ', followed by the value of the text variable
    or the default 'is cool', underscores replaced with spaces.
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """ Display 'n is a number' only if n is an integer. """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display an HTML page only if n is an integer, with an H1
    tag displaying the number.
    """
    return render_template('number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
