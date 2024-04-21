#!/usr/bin/python3
"""
A simple Flask application to serve a single route displaying 'Hello HBNB!'.
The application is configured to listen on all network interfaces and on port 5000.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns a greeting 'Hello HBNB!' as plain text. """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
