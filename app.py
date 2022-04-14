from flask import Flask
import json

app = Flask(__name__)

with open("candidates.json", "r", encoding="utf-8") as cand_file:
    candidates_mas = json.load(cand_file)


@app.route("/")
def all_cand():
    for i in range(len(candidates_mas)):
        print(f"<pre>"
              f"Имя кандидата - {candidates_mas[i]['name']}\n"
              f"Позиция кандидата - {candidates_mas[i]['position']}\n"
              f"Навыки - {candidates_mas[i]['skills']}</pre>"
              )


@app.route("/candidates/<int:x>/")
def candidate(x):
    return f"<img src='{candidates_mas[{x}]['position']}'>\n<pre>Имя кандидата - {candidates_mas[{x}]['name']}\nПозиция кандидата - {candidates_mas[{x}]['position']}\nНавыки - {candidates_mas[{x}]['skills']}</pre>"


#
@app.route("/skills/<x>")
def page_feed(x):
    for i in range(len(candidates_mas)):
        if x.lower() in candidates_mas[i]['skills'].lower():
            print(f"<pre>"
                  f"Имя кандидата - {candidates_mas[i]['name']}\n"
                  f"Позиция кандидата - {candidates_mas[i]['position']}\n"
                  f"Навыки - {candidates_mas[i]['skills']}</pre>"
                  )


app.run()
