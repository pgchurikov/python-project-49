import random
import math


def gcd(a, b):
    return str(math.gcd(a, b))


def gcd_condition():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f'Question: {a} {b}'
    answer = gcd(a, b)
    return answer, question
