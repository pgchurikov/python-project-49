import random
import math
from brain_games.constant import GAME_INSTRUCTIONS


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def condition():
    number = random.randint(1, 100)
    question = f'Question: {number}'
    answer = 'yes' if is_prime(number) else 'no'
    return answer, question


RULES = GAME_INSTRUCTIONS["prime"]
