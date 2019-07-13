import jinja2
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
        p = Process(target=simp_filt, args=())
        p.start()
        p.join()


app.run()