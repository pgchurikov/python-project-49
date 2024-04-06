import random
from brain_games.cli import welcome_user
from brain_games.constant import GREETINGS
from brain_games.constant import GAME_INSTRUCTIONS
from brain_games.constant import WRONG


def calc_game():
    print('brain-calc\n')
    print(f'{GREETINGS}')
    name = welcome_user()
    print(GAME_INSTRUCTIONS["calc"])
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        operator_list = ['+', '-', '*']
        operator = random.choice(operator_list)
        match operator:
            case '+':
                answer = a + b
            case '-':
                answer = a - b
            case _:
                answer = a * b
        print(f'Question: {a} {operator} {b} = ..')
        user_answer = float(input('Your answer '))
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print(f'\'{user_answer}\'{WRONG}\'{answer}\'')
            print(f'Let\'s try again, {name}!')
            break
    if corrects == 3:
        print(f'Congratulations, {name}!')
