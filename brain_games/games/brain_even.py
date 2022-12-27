#!/usr/bin/env python3
from brain_games.engine import generate_number
import prompt


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    number = generate_number()
    question = f'Question: {number}'
    return question


def get_user_answer():
    user_answer = prompt.string()
    return user_answer


def correct_answer(question):
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no' 
    return correct_answer