from random import randint
from random import choice


DESCRIPTION = 'What is the result of the expression?'
signs = ['+', '-', '*']


def make_question():
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    random_sign = choice(signs)
    question = f'{number1} {random_sign} {number2}'
    return question


def correct_answer(question):
    if signs[0] in question:
        my_numbers = question.split('+')
        correct_answer = int(my_numbers[0]) + int(my_numbers[1])
    elif signs[1] in question:
        my_numbers = question.split('-')
        correct_answer = int(my_numbers[0]) - int(my_numbers[1])
    else:
        my_numbers = question.split('*')
        correct_answer = int(my_numbers[0]) * int(my_numbers[1])
    return str(correct_answer)
