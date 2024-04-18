from brain_games.random import random_100
import math
from brain_games.constant import GAME_INSTRUCTIONS


def gcd(a, b):
    return math.gcd(a, b)


def condition():
    a = random_100()
    b = random_100()
    question = f'Question: {a} {b}'
    answer = str(gcd(a, b))
    return answer, question


RULES = GAME_INSTRUCTIONS["gcd"]
