import jinja2
from werkzeug.utils import secure_filename
import tempfile
from prepare import prepare
from flask import Flask
from flask import render_template, request, redirect
from multiprocessing import Process
from module import simp_filt

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

@app.route("/import", methods=["GET", "POST"])
def index():
    if request.method.lower() == "get":
        return render_template('import.html')
    else:
        file = request.files['file']
        temp_file = secure_filename(file.filename)
        file.save('tmp/', temp_file)
        p = Process(target=simp_filt, args=(prepare.get_json(open('tmp/'+temp_file)),))
        p.start()
        p.join()


app.run()