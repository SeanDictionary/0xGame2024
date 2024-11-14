import pickle
from flask import Flask, request
from base64 import b64decode

app = Flask(__name__)
UserPool = {}
BlackList = [b'\x00', b'\x1e', b'system', b'popen', b'os', b'sys', b'posix']


class User:
    username = None
    password = None


@app.route('/')
def index():
    return open(__file__).read()


@app.route('/login', methods=['POST'])
def login():
    data = request.form.get('data')
    if data is not None:
        opcode = b64decode(data)
        for word in BlackList:
            if word in opcode:
                return "Hacker!"
        user = pickle.loads(opcode)
        print(user)
        return "<h1>Hello {}</h1>".format(user.username)
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username in UserPool.keys() and password == UserPool[username].password:
            return "<h1>Hello {}</h1>".format(User.username)


@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in UserPool.keys():
        return "<h1>用户{}已存在</h1>".format(username)
    UserPool[username] = password
    return "<h1>注册成功</h1>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
