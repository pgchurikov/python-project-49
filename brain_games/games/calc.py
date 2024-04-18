import random
from brain_games.constant import GAME_INSTRUCTIONS


def condition():
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


RULES = GAME_INSTRUCTIONS["calc"]
