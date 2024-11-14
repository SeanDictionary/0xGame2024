from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    print(request.user_agent.string.lower().find("mozi"))
    return open(__file__).read()


@app.route('/fileread')
def read_file():
    filename = request.args.get('filename')
    return open(filename).read()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
