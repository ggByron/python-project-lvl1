#!/usr/bin/env python3
from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question():
    number1 = randint(1, 25)
    number2 = randint(1, 25)
    question = f'Question: {number1} {number2}'
    return question


def correct_answer(question):
    my_numbers = question[9:].split()
    my_gcd = str(gcd(int(my_numbers[0]), int(my_numbers[1])))
    return my_gcd
