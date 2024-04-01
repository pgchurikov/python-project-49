#!/usr/bin/env python3


import prompt
import random


a = 0


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 100)
        if a % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        print(f'Question: {a}')
        user_answer = prompt.string('Your answer ')
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{answer}\'')
            print(f'Let\'s play again, {name}')
            break
    if corrects == 3:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    print('brain-even')
    main()
