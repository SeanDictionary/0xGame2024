import flask
from flask import *
import os
import jwt
from key import KEY, FLAG

users = {}
app = flask.Flask(__name__)


@app.route("/")
def index():
    file_path = os.path.abspath(__file__)
    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()
    return render_template("index.html", code=code)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        role = "guest"
        if username in users:
            return "User already exists"
        users[username] = {"password": password, "role": role}
        return redirect(url_for("login"), code=302)
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username not in users:
            return "User does not exist"
        if users[username]["password"] != password:
            return "Invalid password"
        payload = {"username": username, "role": users[username]["role"]}
        try:
            token = jwt.encode(payload, KEY, algorithm="HS256")
            response = make_response(redirect(url_for("flag"), code=302))
            response.set_cookie("token", token)
            return response
        except Exception as e:
            return str(e)
    return render_template("login.html")


@app.route("/flag", methods=["GET"])
def flag():
    token = request.cookies.get("token")
    if not token:
        return redirect(url_for("login"), code=302)
    try:
        payload = jwt.decode(token, KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"
    if payload["role"] != "admin":
        return "Only admin can view the flag"
    return FLAG


@app.route("/hint1", methods=["GET"])
def hint1():
    token = request.cookies.get("token")
    if not token:
        return redirect(url_for("login"), code=302)
    try:
        payload = jwt.decode(
            token, KEY, algorithms=["HS256"], options={"verify_signature": False}
        )
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"
    if payload["role"] != "Please, give me the hint":
        return "Beg me for the hint"
    return render_template("hint1.html")


@app.route("/hint2", methods=["GET"])
def hint2():
    tmp_key = (
        "Very very long and include many !@#$)*$&@) so you can't crack's secret key"
    )
    token = request.cookies.get("token")
    if not token:
        return redirect(url_for("login"), code=302)
    try:
        payload = jwt.decode(token, tmp_key, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"
    if payload["role"] != "But, I can see the temporary key":
        return "Beg me for the hint"
    return render_template("hint2.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
