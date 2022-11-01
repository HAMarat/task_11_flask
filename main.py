from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, \
    get_candidates_by_skill

app = Flask(__name__)

PATH_FILE = 'candidates.json'
candidates_data: list[dict] = load_candidates_from_json(PATH_FILE)


@app.route('/')
def candidates():
    """
    Отображаем список всех кандидатов
    """
    return render_template('list.html',
                           candidates=candidates_data,
                           )


@app.route('/candidate/<candidate_id>')
def candidate_page(candidate_id: str):
    """
    Отображаем информацию о выбранном кандидате
    """
    if not candidate_id.isdigit():
        return "Такого пользователя нет"
    candidate = get_candidate(candidates_data, candidate_id)
    if candidate:
        return render_template('single.html',
                               candidate=candidate,
                               )
    return "Такого пользователя нет"


@app.route('/search/<candidate_name>')
def candidate_search(candidate_name: str):
    """
    Отображаем информацию о найденных по имени кандидатах
    """
    candidates_by_name = get_candidates_by_name(candidates_data, candidate_name)
    if candidates_by_name:
        return render_template('search.html',
                               candidates_by_name=candidates_by_name,
                               )
    return "Пользователей с таким именем нет"


@app.route('/skill/<skill_name>')
def candidate_by_skill(skill_name: str):
    """
    Отображаем информацию о найденных по навыку кандидатах
    """
    candidates_by_skill = get_candidates_by_skill(candidates_data, skill_name)
    if candidates_by_skill:
        return render_template('skill.html',
                               skill_name=skill_name,
                               candidates_by_skill=candidates_by_skill,
                               )
    return "<center>Пользователей с таким навыком нет</center>"


app.run(host='127.0.0.1', port=3000)
