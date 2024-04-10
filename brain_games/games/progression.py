import random
from brain_games.core import play_game
from brain_games.constant import GAME_INSTRUCTIONS


def progression():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    lenght = random.randint(5, 10)
    index = random.randint(0, lenght - 1)
    list = []
    for _ in range(lenght):
        list.append(a)
        a += b
    answer = str(list[index])
    list[index] = '..'
    hidden_progression = ' '.join(map(str, list))
    question = f'Question: {hidden_progression}'
    return answer, question


def progression_game():
    print('brain-progression\n')
    play_game(progression, GAME_INSTRUCTIONS["progression"])
