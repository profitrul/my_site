from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'hello'

@app.route("/name/<text>")
def name(text):
    return 'hello ' +text

if __name__ == '__main__':
    app.run()