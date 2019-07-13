import jinja2
from werkzeug.utils import secure_filename
import tempfile
import json
from flask import Flask
from flask import render_template, request, redirect
from multiprocessing import Process
from module import prepare, simp_filt

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

@app.route("/import", methods=["GET", "POST"])
def index():
    if request.method.lower() == "get":
        return render_template('import.html')
    else:
        file = request.files['file']
        temp_file = secure_filename(file.filename)
        file.save('tmp/'+temp_file)
        target = simp_filt.parsing(prepare.get_json('tmp/'+temp_file))
        simp_filt.flush_to_db(request.cookies.get('id'), json.dumps(target))


app.run(host="0.0.0.0")