import random
import prompt
import math
from brain_games.constant import GREETINGS
from brain_games.constant import GAME_INSTRUCTIONS
from brain_games.constant import WRONG


def gcd_game():
    print('brain-gcd\n')
    print(f'{GREETINGS}')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(GAME_INSTRUCTIONS["gcd"])
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f'Question: {a} {b}')
        answer = math.gcd(a, b)
        user_answer = int(input('Your answer: '))
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print(f'\'{user_answer}\'{WRONG}\'{answer}\'')
            print(f'Let\'s try again, {name}!')
            break
    if corrects == 3:
        print(f'Congratulations, {name}!')
