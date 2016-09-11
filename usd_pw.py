import os
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash

app=Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'usd_pw.db'),SECRET_KEY='JACOBISGAY',USERNAME='admin',PASSWORD='default'))
app.config.from_envvar('USD_PW_SETTINGS', silent=True)

def connect_db():
    RowVector = sqlite3.connect(app.config['DATABASE'])
    RowVector.row_factory = sqlite3.Row
    return RowVector

def get_db():
    if not hassattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def home():
    return render_template("home.html")
