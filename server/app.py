#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Welcome to FLASK!!</h1>"

@app.route('/<string:username>')
def user(username):
    return f'<h1>Welcome {username}</h1>'

@app.route('/about')
def about():
    return f'<h1>This is the about us page.</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5555)
    # app.run(port=5555)  #- use to specify a specific port