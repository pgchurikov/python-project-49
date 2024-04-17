import random
from brain_games.constant import GAME_INSTRUCTIONS


def is_even(number):
    return number % 2 == 0


def brain_even():
    number = random.randint(1, 100)
    question = f'Question: {number}'
    answer = 'yes' if is_even(number) else 'no'
    instruction = GAME_INSTRUCTIONS["even"]
    return answer, question, instruction
