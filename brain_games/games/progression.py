import random
import prompt


def progression_game():
    print('brain-progression\n')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What number is missing in the progression?')
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        index = random.randint(0, 9)
        list = []
        for _ in range(1, 11):
            list.append(a)
            a += b
        answer = list[index]
        list[index] = '..'
        question = ' '.join(map(str, list))
        print(f'Question:  {question}')
        user_answer = int(input('Your answer '))
        if user_answer == answer:
            print('Correct!')
            corrects += 1
            list.clear()
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{answer}\'')
            print(f'Let\'s try again, {name}!')
            break
    if corrects == 3:
        print(f'Congratulations, {name}!')
