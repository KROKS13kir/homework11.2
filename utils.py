import json


def load_candidates_from_json(path):
    #подгружаем json
    with open(path, "r", encoding="utf-8") as cand_file:
        candidates_mas = json.load(cand_file)
    return candidates_mas


def get_candidate(candidate_id):
    #находим кандидата под номером candidate_id
    candidates_mas = load_candidates_from_json('candidates.json')
    for candidate in candidates_mas:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    #находим имя кандидата
    candidates_mas = load_candidates_from_json('candidates.json')
    result = []
    for candidate in candidates_mas:
        cand_name = candidate['name'].lower().split(' ')
        if candidate_name.lower() in cand_name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    #ищем навык у всех
    candidates_mas = load_candidates_from_json('candidates.json')
    result = []
    for candidate in candidates_mas:
        cand_skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in cand_skills:
            result.append(candidate)
    return result
