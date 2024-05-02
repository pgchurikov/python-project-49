import random


def get_answer_and_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator_list = ['+', '-', '*']
    operator = random.choice(operator_list)
    match operator:
        case '+':
            answer = str(a + b)
        case '-':
            answer = str(a - b)
        case _:
            answer = str(a * b)
    question = f'Question: {a} {operator} {b} = ..'
    return answer, question


RULES = 'What is the result of the expression?'
