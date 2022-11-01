from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

PATH_FILE = 'candidates.json'
candidates_data = load_candidates_from_json(PATH_FILE)


@app.route('/')
def candidates():
    return render_template('list.html',
                           candidates=candidates_data,
                           )


@app.route('/candidate/<candidate_id>')
def candidate_page(candidate_id):
    if not candidate_id.isdigit():
        return f"Такого пользователя нет"
    candidate = get_candidate(candidates_data, candidate_id)
    if candidate:
        return render_template('single.html',
                               candidate=candidate,
                               )
    return f"Такого пользователя нет"


@app.route('/search/<candidate_name>')
def candidate_page(candidate_name):
    candidates_by_name = get_candidates_by_name(candidates_data, candidate_name)
    if candidates_by_name:
        return render_template('search.html',
                               candidates=candidates_by_name,
                               )
    return f"Пользователей с таким именем нет"


app.run(host='127.0.0.1', port=2000)
