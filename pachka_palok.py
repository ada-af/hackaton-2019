import jinja2
from werkzeug.utils import secure_filename
import tempfile
import json
import random
from flask import Flask
from flask import render_template, request, redirect, make_response
from multiprocessing import Process
from module import prepare, simp_filt, nn_class
from hashlib import md5
import sqlite3
import os

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

def dhfskjfgs(temp_file, remote_addr):
    adv_tgt = nn_class.evaluate_topics(prepare.get_json('tmp/'+temp_file))
    prepare.update_adv_filt(remote_addr, adv_tgt)

@app.route("/import", methods=["GET", "POST"])
def importer():
    if request.method.lower() == "get":
        return render_template('import.html')
    else:
        file = request.files['file']
        temp_file = str(random.randint(10000, 10000000))+".tgz"
        file.save('tmp/'+temp_file)
        target = simp_filt.parsing(prepare.get_json('tmp/'+temp_file))
        simp_filt.flush_to_db(request.remote_addr, json.dumps(target))
        dhfskjfgs(temp_file, request.remote_addr)
        os.remove("tmp/"+temp_file)
        return redirect('/dash')

@app.route("/dash", methods=['GET'])
def dash():
    return render_template("dashboard.html", j=prepare.get_db_entry(request.remote_addr), str=str)

@app.route("/sign/in", methods=['POST'])
def sign_in():
    if request.method.lower() == 'post':
        user = request.form['user']
        passwd = md5(request.form['passwd']).hexdigest()
        conn = sqlite3.connect('sqlite.db')
        cur = conn.cursor()
        data = cur.execute("select count(*), user_sec from users where username='{}' and passwd='{}'".format(user, passwd))
        if data[0][0] == 0:
            resp = make_response(redirect('/dash'))
            resp.set_cookie('user_sec', data[0][1])
            return resp
        else:
            return redirect('/')

@app.route("/sign/up", methods=["POST"])
def sign_up():        
    if request.method.lower() == 'post':
        user = request.form['user']
        passwd = md5(request.form['passwd']).hexdigest()
        conn = sqlite3.connect('sqlite.db')
        cur = conn.cursor()
        user_sec = md5(str(random.randint(0, 100000))+passwd).hexdigest()
        try:
            cur.execute("insert into users values('{}','{}','{}'".format(user, passwd,
            user_sec))
        except Exception:
            return redirect('/')
        else:
            resp = make_response(redirect('/dash'))
            resp.set_cookie('user_sec', user_sec)
            return resp
        

@app.route("/")
def index():
    return render_template('index.html')

app.run(host="0.0.0.0")