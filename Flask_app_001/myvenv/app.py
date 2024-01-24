from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'Nikhil Vedpathak'


if __name__ == "__main__":
    app.run()