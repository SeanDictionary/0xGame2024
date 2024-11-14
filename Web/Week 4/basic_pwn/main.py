from flask import Flask, request

app = Flask(__name__)

functions=globals()['__builtins__'].__dict__


@app.route('/', methods=['GET'])
def index():
    return open(__file__).read()

@app.route('/pwn',methods=['POST'])
def pwn():
    stack = []
    stack.append('print')
    name=request.get_json().get("name")
    if not name:
        return "Fail"
    stack.extend(name)
    args=stack.pop()
    func=stack.pop()
    functions[func](args)
    return "Success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)