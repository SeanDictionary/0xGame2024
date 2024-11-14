from flask import Flask, request
import json

app = Flask(__name__)

'''
'''
def merge(src, dst):
    # Recursive merge function
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)


class Dst():
    def __init__(self):
        pass


dst = Dst()


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return open("main.py").read()
    merge(request.get_json(), dst)
    return "Success"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
