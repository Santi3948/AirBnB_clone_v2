#!/usr/bin/python3
"""hbnb module"""
from flask import Flask, escape, request, render_template

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


@app.route('/python')
@app.route('/python/<text>')
def hello4(text="is cool"):
    """Hello Python"""
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>')
def hello5(n):
    """Hello n!!!"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def hello6(n):
    """Hello n again!!!"""
    return render_template('5-number.html', var=n)


if __name__ == "__main__":
    app.run()
