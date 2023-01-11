from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    for _ in range(2, number // 2 + 1):
        if number % _ == 0:
            return False
    return True


def make_qstn_and_answer():
    number = randint(1, 99)
    question = f'{number}'
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return [question, answer]
