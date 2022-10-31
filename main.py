from flask import Flask
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

PATH_FILE = 'candidates.json'
candidates_data = load_candidates_from_json(PATH_FILE)


@app.route('/')
def candidates():
    candidates_data_return = ['<h1>Все кандидаты</h1>']
    for candidate in candidates_data:
        candidate_data = f'<p><a href="/candidate/<x>">{candidate["picture"]}</a></p>'

