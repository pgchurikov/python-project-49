import random
import math
from brain_games.core import play_game
from brain_games.constant import GAME_INSTRUCTIONS


def prime():
    a = random.randint(1, 100)
    question = f'Question: {a}'
    answer = 'yes'
    if a <= 1:
        answer = 'no'
    i = 2
    while i <= math.sqrt(a):
        if a % i == 0:
            answer = 'no'
            break
        i += 1
    return answer, question


def prime_game():
    print('brain-prime\n')
    play_game(prime, GAME_INSTRUCTIONS["prime"])
