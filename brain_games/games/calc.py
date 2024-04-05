import random
import prompt


def calc_game():
    print('brain-calc\n')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
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
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{answer}\'')
            print(f'Let\'s try again, {name}!')
            break
    if corrects == 3:
        print(f'Congratulations, {name}!')
