#!/usr/bin/env python3
from brain_games.engine import generate_number


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    number = generate_number()
    question = f'Question: {number}'
    return question


def correct_answer(question):
    number = int(question[9:])
    divisor = 2
    correct_answer = 'yes'
    while divisor <= number:
        if number % divisor == 0:
            correct_answer = 'no'
            return correct_answer
        else:
            divisor += 1
    return correct_answer
