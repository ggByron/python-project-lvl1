#!/usr/bin/env python3
from brain_games.engine import generate_number


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    number = generate_number()
    question = f'Question: {number}'
    return question


def correct_answer(question):
    if int(question[-2:]) % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
