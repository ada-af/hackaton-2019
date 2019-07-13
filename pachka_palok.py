import jinja2
from werkzeug.utils import secure_filename
import tempfile
import json
import random
from flask import Flask
from flask import render_template, request, redirect
from multiprocessing import Process
from module import prepare, simp_filt

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

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
        return redirect('/dash')

@app.route("/dash", methods=['GET'])
def dash():
    return render_template("dashboard.html", j=prepare.get_db_entry(request.remote_addr), str=str)

@app.route("/")
def index():
    return render_template('index.html')

app.run(host="0.0.0.0")