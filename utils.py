import json


def load_candidates_list_from_json(path="candidates.json"):
    """возвращает список всех кандидатов"""
    with open(path, "r", encoding="utf-8") as file:
        candidates_list = json.load(file)
    return candidates_list


# def load_candidates_list(candidates_list):
#     """возвращает список всех кандидатов"""
#     candidates = '<pre>'
#     for candidate in candidates_list:
#         candidates += (f'Имя кандидата - {candidate["name"]}\n'
#                        f'Позиция кандидата - {candidate["picture"]}\n'
#                        f'Позиция кандидата - {candidate["position"]}\n'
#                        f'Позиция кандидата - {candidate["gender"]}\n'
#                        f'Позиция кандидата - {candidate["age"]}\n'
#                        f'Навыки - {candidate["skills"]}\n\n')
#     candidates += '</pre>'
#     return candidates


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    candidates = load_candidates_list_from_json()
    this_candidate = {}
    for candidate in candidates:
        if candidate_id == candidate["id"]:
            this_candidate = candidate
    return this_candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidates = load_candidates_list_from_json()
    this_candidates = []
    for candidate in candidates:
        cn1, cn2 = candidate["name"].split(" ")
        if candidate_name.lower() == cn1.lower():
            this_candidates.append(candidate)
    return this_candidates


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidates = load_candidates_list_from_json()
    this_candidates = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower():
            this_candidates.append(candidate)
    return this_candidates


#print(load_candidates_list_from_json("candidates.json"))
#
#print(load_candidates_list(load_candidates_list_from_json("candidates.json")))
#
#print(get_candidate(10))
#
#print(get_candidates_by_name("Sheri"))
#
print(get_candidates_by_skill("python"))
