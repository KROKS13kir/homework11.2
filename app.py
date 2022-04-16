from flask import Flask
import json

app = Flask(__name__)

with open("candidates.json", "r", encoding="utf-8") as cand_file:
    candidates_mas = json.load(cand_file)


@app.route("/")
def all_cand():
    result = '<pre>'
    for i in range(len(candidates_mas)):
        result += (f"<pre>"
                   f"Имя кандидата - {candidates_mas[i]['name']}\n"
                   f"Позиция кандидата - {candidates_mas[i]['position']}\n"
                   f"Навыки - {candidates_mas[i]['skills']}\n\n"
                   )
    result += '<pre>'
    return result


@app.route("/candidates/<int:x>")
def candidate(x):
    temp = candidates_mas[x]['picture'].replace('"', '')
    return f"<img src= '{temp}'>\n<pre>Имя кандидата - {candidates_mas[x]['name']}\nПозиция кандидата - {candidates_mas[x]['position']}\nНавыки - {candidates_mas[x]['skills']}</pre>"


@app.route("/skills/<x>/")
def page_feed(x):
    result = '<pre>'
    for i in range(len(candidates_mas)):
        cand_skills = candidates_mas[i]['skills'].lower().split(', ')
        if x in cand_skills:
            result += (f"Имя кандидата - {candidates_mas[i]['name']}\n"
                       f"Позиция кандидата - {candidates_mas[i]['position']}\n"
                       f"Навыки - {candidates_mas[i]['skills']}\n\n"
                       )
    result += '<pre>'
    return result


app.run()
