from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_qstn_and_answer():
    number1 = randint(1, 25)
    number2 = randint(1, 25)
    question = f'{number1} {number2}'
    answer = str(gcd(number1, number2))
    return [question, answer]
