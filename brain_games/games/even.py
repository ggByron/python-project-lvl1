from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_qstn_and_answer():
    number = randint(1, 100)
    question = f'{number}'
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return [question, answer]
