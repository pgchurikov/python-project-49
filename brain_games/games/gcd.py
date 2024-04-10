import random
import math
from brain_games.core import play_game
from brain_games.constant import GAME_INSTRUCTIONS


def gcd():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f'Question: {a} {b}'
    answer = str(math.gcd(a, b))
    return answer, question


def gcd_game():
    print('brain-gcd\n')
    play_game(gcd, GAME_INSTRUCTIONS["gcd"])
