from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    number = randint(1, 100)
    question = f'Question: {number}'
    return question


def correct_answer(question):
    if int(question[-2:]) % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
