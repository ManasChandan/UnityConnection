from flask import Flask, redirect, url_for, request, render_template , jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/post', methods =['GET','POST'])
def post():
    jsonRequest = request.json
    print(jsonRequest)
    output = int(jsonRequest['num'])
    return jsonify({'output': str(output + 5)})


if __name__ == '__main__':
    app.run(debug=True)
