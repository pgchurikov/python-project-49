import random


def random_100():
    number = random.randint(1, 100)
    return number


def lenght_and_index():
    lenght = random.randint(5, 10)
    index = random.randint(0, lenght - 1)
    return lenght, index


def random_10():
    number, step = random.randint(1, 10), random.randint(1, 10)
    return number, step
