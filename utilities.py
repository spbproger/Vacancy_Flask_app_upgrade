import json


def load_candidates_list_from_json(path="candidates.json"):
    """возвращает список всех кандидатов"""
    with open(path, "r", encoding="utf-8") as file:
        candidates_list = json.load(file)
    return candidates_list


def load_candidates_list(candidates_list):
    """возвращает список всех кандидатов"""
    candidates = '<pre>'
    for candidate in candidates_list:
        candidates += (f'Имя кандидата - {candidate["name"]}\n'
                       f'Позиция кандидата - {candidate["picture"]}\n'
                       f'Позиция кандидата - {candidate["position"]}\n'
                       f'Позиция кандидата - {candidate["gender"]}\n'
                       f'Позиция кандидата - {candidate["age"]}\n'
                       f'Навыки - {candidate["skills"]}\n\n')
    candidates += '</pre>'
    return candidates


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    candidates = load_candidates_list_from_json()
    candidate = '<pre>\n'
    for item in candidates:
        if item["id"] == candidate_id:
            candidate += (f'Имя кандидата - {item["name"]}\n'
                          f'Позиция кандидата - {item["picture"]}\n'
                          f'Позиция кандидата - {item["position"]}\n'
                          f'Позиция кандидата - {item["gender"]}\n'
                          f'Позиция кандидата - {item["age"]}\n'
                          f'Навыки - {item["skills"]}\n')
    candidate += '</pre>'
    return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidates = load_candidates_list_from_json()
    candidate = '<pre>\n'
    for item in candidates:
        if item["name"] == candidate_name:
            candidate += (f'Имя кандидата - {item["name"]}\n'
                          f'Позиция кандидата - {item["picture"]}\n'
                          f'Позиция кандидата - {item["position"]}\n'
                          f'Позиция кандидата - {item["gender"]}\n'
                          f'Позиция кандидата - {item["age"]}\n'
                          f'Навыки - {item["skills"]}\n')
    candidate += '</pre>'
    return candidate


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidates = load_candidates_list_from_json()
    candidate = '<pre>\n'
    for item in candidates:
        if skill_name.lower() in item["skills"].lower():
            candidate += (f'Имя кандидата - {item["name"]}\n'
                          f'Позиция кандидата - {item["picture"]}\n'
                          f'Позиция кандидата - {item["position"]}\n'
                          f'Позиция кандидата - {item["gender"]}\n'
                          f'Позиция кандидата - {item["age"]}\n'
                          f'Навыки - {item["skills"]}\n\n')
    candidate += '</pre>'
    return candidate

# print(load_candidates_list_from_json("candidates.json"))
#
# print(load_candidates_list(load_candidates_list_from_json("candidates.json")))
#
# print(get_candidate(5))
#
# print(get_candidates_by_name("Day Holloway"))
#
# print(get_candidates_by_skill("python"))