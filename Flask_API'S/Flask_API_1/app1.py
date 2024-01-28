# Simple Greet API
from flask import Flask, jsonify, render_template, url_for

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("home.html")

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({'message': 'Hello, welcome to the REST API!'})

if __name__ == '__main__':
    app.run(debug=True)
