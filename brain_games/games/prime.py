import random
import math
import prompt
from brain_games.constant import GREETINGS
from brain_games.constant import GAME_INSTRUCTIONS
from brain_games.constant import WRONG


def is_prime():
    a = random.randint(1, 100)
    print(f'Question: {a}')
    answer = 'yes'
    if a <= 1:
        answer = 'no'
    i = 2
    while i <= math.sqrt(a):
        if a % i == 0:
            answer = 'no'
            break
        i += 1
    return (answer)


def prime_game():
    print('brain-prime\n')
    print(f'{GREETINGS}')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(GAME_INSTRUCTIONS["prime"])
    corrects = 0
    while corrects < 3:
        answer = is_prime()
        user_answer = input('Your answer ')
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print(f'\'{user_answer}\'{WRONG}\'{answer}\'')
            print(f'Let\'s try again, {name}!')
            break
        if corrects == 3:
            print(f'Congratulations, {name}!')
