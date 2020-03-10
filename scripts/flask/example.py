from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        print(request.args)
        return 'Hello, request!'
    elif request.method == 'GET':
        return 'Hello, GET!'


if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host=127.0.0.1, port=5000, debug=false
    # http://127.0.0.1:18000/
    app.run(port=18000)
