from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Hello Guy, lets begin with flask"

@app.route('/api/<name>')

def name(name):
    print(name)
    return "Hello Guy, lets begin with api"


if __name__ == '__main__':
    app.run(debug=True)