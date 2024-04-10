import random
from brain_games.core import play_game
from brain_games.constant import GAME_INSTRUCTIONS


def even():
    a = random.randint(1, 100)
    if a % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    question = f'Question: {a}'
    return answer, question


def even_game():
    print('brain-even\n')
    play_game(even, GAME_INSTRUCTIONS["even"])
