from flask import Flask, request, render_template
from utils import load_candidates_list_from_json, get_candidate

app = Flask(__name__)

candidates = load_candidates_list_from_json()


@app.route('/')
def index():
    return render_template("list.html", candidates=candidates)


@app.route('/candidates/<candidate_id>/')
def search_by_id(candidate_id):
    # item = get_candidate(candidates, candidate_id)
    # return render_template("single.html", item=item)
    return render_template("single.html", candidates=candidates, candidate_id=candidate_id)


@app.route('/search/<candidate_name>/')
def search_by_name(candidate_name):
    return render_template("search.html", candidates=candidates, candidate_name=candidate_name)


@app.route('/search/<candidate_name>')
def search_by_skills(candidate_skills):
    return render_template("skill.html", candidates=candidates, candidate_name=candidate_skills)


app.run()
