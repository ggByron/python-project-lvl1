from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_qstn_and_answer():
    number = randint(1, 99)
    question = f'{number}'
    if number == 1:
        answer = 'no'
        return [question, answer]
    elif number == 2:
        answer = 'yes'
        return [question, answer]
    else:
        divisor = 2
        while divisor <= (number / 2 + 1):
            if number % divisor == 0:
                answer = 'no'
                return [question, answer]
            else:
                divisor += 1
        answer = 'yes'
    return [question, answer]
