import random
from brain_games.cli import welcome_user
from brain_games.constant import GREETINGS
from brain_games.constant import GAME_INSTRUCTIONS
from brain_games.constant import WRONG


def even_game():
    print('brain-even\n')
    print(f'{GREETINGS}')
    name = welcome_user()
    print(GAME_INSTRUCTIONS["even"])
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 100)
        if a % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        print(f'Question: {a}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print(f'\'{user_answer}\'{WRONG}\'{answer}\'')
            print(f'Let\'s try again, {name}!')
            break
    if corrects == 3:
        print(f'Congratulations, {name}!')
