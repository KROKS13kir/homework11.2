from flask import Flask, render_template
import utils



app = Flask(__name__)


@app.route("/")
def all_cand():
    #список всех кандидатов
    cands_mas = utils.load_candidates_from_json("candidates.json")
    return render_template("list.html", cands_mas=cands_mas)


@app.route("/candidates/<int:x>/")
def candidate_number(x):
    #вся информация о человеке под определённым номером
    cand = utils.get_candidate(x)
    return render_template("card.html", cand=cand)

@app.route("/search/<candidate_name>")
def cand_name(candidate_name):
    name_cand = utils.get_candidates_by_name(candidate_name)
    length_programmers = len(name_cand) #кол-во людей с определённым именем
    return render_template("search.html", length_programmers=length_programmers, name_cand=name_cand)

@app.route("/skills/<skill_name>/")
def page_skill(skill_name):
    skill_cands_mas = utils.get_candidates_by_skill(skill_name)
    length = len(skill_cands_mas) #кол-во людей с определённым скиллом
    return render_template("skill.html", skill=skill_name, length=length, skill_cands_mas=skill_cands_mas)


app.run()
