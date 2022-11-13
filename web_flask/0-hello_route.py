#!/usr/bin/python3
"""
Script starts a Flask Web Application
Runs on `Port: 5000, host: 0.0.0.0`
Route implements strict_slashes=False
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Function called with / route
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
