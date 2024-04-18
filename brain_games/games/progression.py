from brain_games.random import random_10, lenght_and_index
from brain_games.constant import GAME_INSTRUCTIONS


def progression(number, step, lenght):
    list = []
    for _ in range(lenght):
        list.append(number)
        number += step
    return list


def number_to_hide():
    number, step = random_10()
    lenght, index = lenght_and_index()
    list = progression(number, step, lenght)
    return index, list


def condition():
    index, list = number_to_hide()
    answer = str(list[index])
    list[index] = '..'
    hidden_progression = ' '.join(map(str, list))
    question = f'Question: {hidden_progression}'
    return answer, question


RULES = GAME_INSTRUCTIONS["progression"]
