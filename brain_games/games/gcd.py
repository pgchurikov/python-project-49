import random
import prompt
import math

def gcd_game():
    print('brain-gcd\n')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Find the greatest common divisor of given numbers.')
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f'Question: {a}, {b}')
        answer = math.gcd(a, b)
        user_answer = int(input('Your answer: '))
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{answer}\'')
            print(f'Let\'s play again, {name}!')
            break
    if corrects == 3:
        print(f'Congratulations, {name}!')
