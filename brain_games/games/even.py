import random


def is_even(number):
    return number % 2 == 0


def get_answer_and_question():
    number = random.randint(1, 100)
    question = f'Question: {number}'
    answer = 'yes' if is_even(number) else 'no'
    return answer, question


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
