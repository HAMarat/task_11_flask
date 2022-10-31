from flask import Flask
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

PATH_FILE = 'candidates.json'
candidates_data = load_candidates_from_json(PATH_FILE)
