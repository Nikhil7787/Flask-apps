#Accepting POST Requests

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['POST'])
def add_numbers():
    data = request.get_json()
    result = data['number1'] + data['number2']
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
