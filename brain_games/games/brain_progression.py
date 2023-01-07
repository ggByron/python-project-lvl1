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
    question = str(progression)
    question = question[1:-1]
    question = question.replace(',', "")
    question = question.replace('\'', "")
    return question


def correct_answer(question):
    progression = list(question.split(' '))
    missing_elem_index = progression.index('..')
    elem_before = int(progression[missing_elem_index - 1])
    elem_after = int(progression[missing_elem_index + 1])
    missing_elem = int((elem_before + elem_after) / 2)
    return str(missing_elem)
