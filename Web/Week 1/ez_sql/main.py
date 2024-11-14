import os
import sqlite3
from dataclasses import dataclass

from flask import Flask, request, render_template,redirect

app = Flask(__name__)
app.template_folder = 'templates'


@dataclass
class User:
    id: int
    username: str
    email: str
    phone: str
    address: str


@app.before_request
def before_request():
    if request.user_agent.string.lower().find("sqlmap") >= 0:
        return "hacker"
    id = request.args.get('id') or 1
    if isinstance(id, str) and (id.find('\"') > 0 or id.find('\'') > 0):
        return "hacker"

@app.route('/')
def index():
    global result,error
    id = request.args.get('id')
    if id==None:
        return redirect("/?id=1")
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    sql="select * from users where id = "+str(id)
    result = conn.execute(sql).fetchone()
    conn.close()
    return render_template('index.html', user=User(*result), sql=sql)


if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    conn.executescript(open("init.sql").read())
    conn.execute(f"insert into flag(flag) values (?)",(os.getenv('flag'),))
    conn.commit()
    conn.close()

    app.run(host='0.0.0.0', port=8000)
