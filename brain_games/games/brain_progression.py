#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def make_question():
    first_number = randint(1, 10)
    progression = [first_number]
    step = randint(1, 5)
    next_number = first_number + step
    progression_length = 1

    while progression_length < 10:
        progression.append(next_number)
        next_number += step
        progression_length += 1

    missing_elem = randint(1, 8)
    progression[missing_elem] = '..'
    progression = str(progression)
    progression = progression[1:-1]
    progression = progression.replace(',',"")
    progression = progression.replace('\'',"")
    progression = 'Question: ' + progression
    return progression


def correct_answer(question):
    progression = list(question.split(' '))
    missing_elem_index = progression.index('..')
    elem_before = int(progression[missing_elem_index - 1])
    elem_after = int(progression[missing_elem_index + 1])
    missing_elem = int((elem_before + elem_after) / 2)
    return str(missing_elem)
