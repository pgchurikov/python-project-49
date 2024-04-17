import random
import math
from brain_games.constant import GAME_INSTRUCTIONS


def gcd(a, b):
    return str(math.gcd(a, b))


def brain_gcd():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f'Question: {a} {b}'
    answer = gcd(a, b)
    instruction = GAME_INSTRUCTIONS["gcd"]
    return answer, question, instruction
