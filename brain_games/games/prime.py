import random
import prompt
import math


def prime_game():
    print('brain-prime\n')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 100)
        answer = 'yes'
        if a <= 1:
            answer = 'no'
        i = 2
        while i <= math.sqrt(a):
            if a % i == 0:
                answer = 'no'
                break
            i += 1
        print(f'Question: {a}')
        user_answer = input('Your answer ')
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{answer}\'')
            print(f'Let\'s try again, {name}!')
            break
        if corrects == 3:
            print(f'Congratulations, {name}!')
