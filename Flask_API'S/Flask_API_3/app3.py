# Handling Path Variables  
from flask import Flask, jsonify, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
   return render_template("home.html")

@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    return jsonify({'username': username})
    

if __name__ == '__main__':
    app.run(debug=True)
