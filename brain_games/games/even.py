from brain_games.random import random_100
from brain_games.constant import GAME_INSTRUCTIONS


def is_even(number):
    return number % 2 == 0


def condition():
    number = random_100()
    question = f'Question: {number}'
    answer = 'yes' if is_even(number) else 'no'
    return answer, question


RULES = GAME_INSTRUCTIONS["even"]
