import random
from brain_games.core import play_game
from brain_games.constant import GAME_INSTRUCTIONS


def calculation():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator_list = ['+', '-', '*']
    operator = random.choice(operator_list)
    match operator:
        case '+':
            answer = str(a + b)
        case '-':
            answer = str(a - b)
        case _:
            answer = str(a * b)
    question = f'Question: {a} {operator} {b} = ..'
    return answer, question


def calc_game():
    print('brain-calc\n')
    play_game(calculation, GAME_INSTRUCTIONS["calc"])
