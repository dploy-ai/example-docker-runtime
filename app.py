from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/post', methods=['POST'])
def post():
    return request.get_json()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
