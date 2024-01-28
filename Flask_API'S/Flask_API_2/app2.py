#Returning JSON Data
from flask import Flask, jsonify, render_template, url_for

app = Flask(__name__)


@app.route('/')
def Home():
    return render_template("home.html")

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'name': 'Nikhil', 'age': 24, 'city': 'Pune'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
