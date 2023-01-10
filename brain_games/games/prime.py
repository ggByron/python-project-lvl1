from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return 'no'
    elif number == 2:
        return 'yes'
    else:
        divisor = 2
        while divisor <= (number / 2 + 1):
            if number % divisor == 0:
                return 'no'
            else:
                divisor += 1
        return 'yes'


def make_qstn_and_answer():
    number = randint(1, 99)
    question = f'{number}'
    answer = is_prime(number)
    return [question, answer]
