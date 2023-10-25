
from flask import Flask, render_template, request,  url_for, flash, redirect 
import sqlite3
from werkzeug.exceptions import abort

def get_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn=get_conn()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id)).fetchall()
    conn.close()
    if post is None:
        abort(404)
    return post
    
app = Flask(__name__)
@app.route('/')
def index():
    conn = get_conn()
    post = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=post)

@app.route('/new_page')
def new_page():
    return "New page"

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello,my friend you are a crazy!"

@app.route('/new_page')
def new_page():
    return "New page"

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello my friend your compute is very normal!"

@app.route('/new_page')
def new_page():
    return "New page"