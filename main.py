from flask import Flask, request, render_template
from utils import load_candidates_list_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

candidates = load_candidates_list_from_json()


@app.route('/')
def index():
    return render_template("list.html", candidates=candidates)


@app.route('/candidates/<int:candidate_id>/')
def search_by_id(candidate_id):
    candidate = get_candidate(candidate_id)
    if candidate is None:
        return render_template("error.html")
    return render_template("single.html", candidate=candidate)


@app.route('/search/<candidate_name>/')
def search_by_name(candidate_name):
    candidates1 = get_candidates_by_name(candidate_name)
    number = len(candidates1)
    return render_template("search.html", candidates=candidates1, candidate_name=candidate_name, number=number)


@app.route('/skill/<skill_name>/')
def search_by_skills(skill_name):
    candidates2 = get_candidates_by_skill(skill_name)
    number = len(candidates2)
    return render_template("skill.html", candidates=candidates2, skill_name=skill_name, number=number)


app.run()
