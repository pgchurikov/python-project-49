import random


def make_progression(initial_term, difference, lenght):
    list = []
    for _ in range(lenght):
        list.append(initial_term)
        initial_term += difference
    return list


def get_answer_and_question():
    initial_term, difference = random.randint(1, 10), random.randint(1, 10)
    lenght = random.randint(5, 10)
    index = random.randint(0, lenght - 1)
    list = make_progression(initial_term, difference, lenght)
    answer = str(list[index])
    list[index] = '..'
    hidden_progression = ' '.join(map(str, list))
    question = f'Question: {hidden_progression}'
    return answer, question


RULES = 'What number is missing in the progression?'
