#!/usr/bin/python3
"""Flask web"""
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


@app.route('/number_odd_or_even/<int:n>')
def hello7(n):
    """Hello n again!!!"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html',
                               var=n, evenodd="even")
    else:
        return render_template('6-number_odd_or_even.html',
                               var=n, evenodd="odd")


if __name__ == "__main__":
    app.run()
