from flask import Flask, request, render_template
from utils import load_candidates_list_from_json

app = Flask(__name__)


@app.route('/a')
def index():
    lc = load_candidates_list_from_json()
    return render_template("list.html", lc=lc)


app.run()