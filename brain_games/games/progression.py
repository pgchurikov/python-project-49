import random
from brain_games.constant import GAME_INSTRUCTIONS


def progression(number, step, lenght):
    list = []
    for _ in range(lenght):
        list.append(number)
        number += step
    return list


def brain_progression():
    number, step = random.randint(1, 10), random.randint(1, 10)
    lenght = random.randint(5, 10)
    list = progression(number, step, lenght)
    index = random.randint(0, lenght - 1)
    answer = str(list[index])
    list[index] = '..'
    hidden_progression = ' '.join(map(str, list))
    question = f'Question: {hidden_progression}'
    instruction = GAME_INSTRUCTIONS["progression"]
    return answer, question, instruction
