#!/usr/bin/env python3
from random import randint
from random import choice


DESCRIPTION = 'What is the result of the expression?'
signs = ['+', '-', '*']


def make_question():
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    random_sign = choice(signs)
    question = f'Question: {number1} {random_sign} {number2}'
    return question


def correct_answer(question):
    my_exp = question[9:]
    if signs[0] in my_exp:
        my_numbers = my_exp.split('+')
        correct_answer = int(my_numbers[0]) + int(my_numbers[1])
    elif signs[1] in my_exp:
        my_numbers = my_exp.split('-')
        correct_answer = int(my_numbers[0]) - int(my_numbers[1])
    else:
        my_numbers = my_exp.split('*')
        correct_answer = int(my_numbers[0]) * int(my_numbers[1])
    return str(correct_answer)
