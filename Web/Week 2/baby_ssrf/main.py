from flask import Flask, request
import os
from urllib.parse import urlparse, urlunparse
import subprocess
import socket

app = Flask(__name__)
BlackList=[
    "127.0.0.1"
]

@app.route('/')
def index():
    return open(__file__).read()


@app.route('/cmd',methods=['POST'])
def cmd():
    if request.remote_addr != "127.0.0.1":
        return "Forbidden"
    if request.method == "GET":
        return "Hello World!"
    if request.method == "POST":
        return os.popen(request.form.get("cmd")).read()


@app.route('/visit')
def visit():
    url = request.args.get('url')
    if url is None:
        return "No url provided"
    url = urlparse(url)
    realIpAddress = socket.gethostbyname(url.hostname)
    if url.scheme == "file" or realIpAddress in BlackList:
        return "Hacker!"
    result = subprocess.run(["curl","-L", urlunparse(url)], capture_output=True, text=True)
    # print(result.stderr)
    return result.stdout


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
