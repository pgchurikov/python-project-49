import random
import math


def gcd(a, b):
    return math.gcd(a, b)


def get_answer_and_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f'Question: {a} {b}'
    answer = str(gcd(a, b))
    return answer, question


RULES = 'Find the greatest common divisor of given numbers.'
