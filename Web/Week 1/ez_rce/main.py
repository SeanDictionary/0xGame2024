from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return open(__file__).read()


@app.route("/calc", methods=['POST'])
def calculator():
    expression = request.form.get('expression') or "114 1000 * 514 + p"
    result = subprocess.run(["dc", "-e", expression], capture_output=True, text=True)
    return result.stdout


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
