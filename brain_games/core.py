from brain_games.constant import GREETINGS
import prompt
from brain_games.constant import WRONG


def play_game(question_and_answer, instruction):
    print(f'{GREETINGS}')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(f'{instruction}')
    corrects = 0
    while corrects < 3:
        answer, question = question_and_answer()
        print(f'{question}')
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
