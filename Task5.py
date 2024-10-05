import random

def random_carriage(coupe_amount=9):
    carriage = []
    coupe = {}
    for place in range(1, coupe_amount * 4 + 1):
        coupe[place] = random.choice([None, 'ч', 'ж'])
        if len(coupe) == 4:
            carriage.append(coupe)
            coupe = {}
    return carriage

def print_carriage(carriage):
    for index, coupe in enumerate(carriage, 1):
        print(index, ':', coupe)

def empty_coupe_list(carriage):
    answer = {}
    for index, coupe in enumerate(carriage, 1):
        if not any(coupe.values()):
            answer[index] = coupe
    return answer

def empty_place_list(carriage):
    answer = []
    for coupe in carriage:
        for place in coupe:
            if not coupe[place]:
                answer.append(place)
    return answer

def empty_lh_place_list(carriage, low=True):
    answer = []
    for coupe in carriage:
        for place in coupe:
            if not coupe[place] and place % 2 == int(low):
                answer.append(place)
    return answer

def empty_places_in_gender_coupe(carriage, gender):
    answer = []
    for coupe in carriage:
        answer1 = []
        for place in coupe:
            if not coupe[place]:
                answer1.append(place)
            elif coupe[place] != gender:
                break
        else:
            if len(answer1) < 4:
                answer += answer1
    return answer