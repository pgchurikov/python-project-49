import random


def is_even(number):
    return number % 2 == 0


def even_condition():
    number = random.randint(1, 100)
    question = f'Question: {number}'
    answer = 'yes' if is_even(number) else 'no'
    return answer, question
