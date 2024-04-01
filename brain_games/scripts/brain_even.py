#!/usr/bin/env python3


from brain_games.cli import welcome_user
import random


a = 0


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 100)
        if a % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        print(f'Question: {a}')
        user_answer = input('Your answer ')
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{answer}\'')
            print('Let\'s play again')
            break
    if corrects == 3:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    print('brain-even')
    main()
