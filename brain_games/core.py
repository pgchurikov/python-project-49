import prompt
from brain_games.constant import NUMBER_OF_ROUNDS


def play_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.RULES)
    corrects = 0
    while corrects < NUMBER_OF_ROUNDS:
        answer, question = game.get_answer_and_question()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{answer}\'')
            print(f'Let\'s try again, {name}!')
            break
    if corrects == NUMBER_OF_ROUNDS:
        print(f'Congratulations, {name}!')
