from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    number = randint(1, 99)
    question = f'{number}'
    return question


def correct_answer(question):
    number = int(question)
    correct_answer = 'yes'
    if number == 1:
        correct_answer = 'no'
        return correct_answer
    if number == 2:
        return correct_answer
    divisor = 2
    while divisor <= (number / 2 + 1):
        if number % divisor == 0:
            correct_answer = 'no'
            return correct_answer
        else:
            divisor += 1
    return correct_answer
