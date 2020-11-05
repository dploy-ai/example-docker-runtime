from flask import Flask, request, jsonify
from iris.predict import predict

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/predict/', methods=['POST'])
def post():
    data = request.get_json()
    return jsonify(predict(data))


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
