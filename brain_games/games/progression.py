import random
import prompt
from brain_games.constant import GREETINGS
from brain_games.constant import GAME_INSTRUCTIONS
from brain_games.constant import WRONG


def progression_game():
    print('brain-progression\n')
    print(f'{GREETINGS}')
    name = prompt('May I have your name? ')
    print(f'Hello, {name}')
    print(GAME_INSTRUCTIONS["progression"])
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        lenght = random.randint(5, 10)
        index = random.randint(0, lenght - 1)
        list = []
        for _ in range(lenght):
            list.append(a)
            a += b
        answer = list[index]
        list[index] = '..'
        question = ' '.join(map(str, list))
        question = question.strip()
        print(f'Question: {question}')
        user_answer = int(input('Your answer '))
        if user_answer == answer:
            print('Correct!')
            corrects += 1
            list.clear()
        else:
            print(f'\'{user_answer}\'{WRONG}\'{answer}\'')
            print(f'Let\'s try again, {name}!')
            break
    if corrects == 3:
        print(f'Congratulations, {name}!')
