#!/usr/bin/python3
"""hbnb module"""
from flask import Flask, escape, request

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello2():
    """Hello HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def hello3(text):
    """Hello var"""
    return 'C %s' % text.replace("_", " ")


if __name__ == "__main__":
    app.run()
