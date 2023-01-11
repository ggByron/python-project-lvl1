from random import randint
from random import choice


DESCRIPTION = 'What is the result of the expression?'


def make_qstn_and_answer():
    signs = ['+', '-', '*']
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    random_sign = choice(signs)
    question = f'{number1} {random_sign} {number2}'

    if random_sign == '+':
        answer = number1 + number2
    elif random_sign == '-':
        answer = number1 - number2
    elif random_sign == '*':
        answer = number1 * number2

    return [question, str(answer)]
