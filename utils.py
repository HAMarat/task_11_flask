import json


def load_candidates_from_json(path: str) -> list[dict]:
    """
    Загружаем данные кандидатов из файла
    """
    with open(path, 'r', encoding='utf-8') as file:
        candidates_data = json.load(file)
        return candidates_data


def get_candidate(candidates: list[dict], candidate_id: int) -> dict | None:
    """
    Возвращаем данные кандидата по полученному id
    """
    for candidate in candidates:
        if candidate_id == candidate['id']:
            return candidate


def get_candidates_by_name(candidates: list[dict], candidate_name: str) -> dict | None:
    """
    Возвращаем данные кандидата по полученному имени
    """
    for candidate in candidates:
        if candidate_name.lower() == candidate['name'].lower():
            return candidate


def get_candidates_by_skill(candidates: list[dict], skill_name: str) -> list[dict] | None:
    """
    Возвращаем данные кандидатов по выбранному навыку
    """
    list_candidates_by_skill = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            list_candidates_by_skill.append(candidate)
    return list_candidates_by_skill
