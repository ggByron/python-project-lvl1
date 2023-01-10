from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def make_qstn_and_answer():
    first_number = randint(1, 10)
    progression = [first_number]
    step = randint(1, 5)
    next_number = first_number + step
    progression_length = 1

    while progression_length < 10:
        progression.append(next_number)
        next_number += step
        progression_length += 1

    missing_elem_index = randint(1, 8)
    answer = str(progression[missing_elem_index])
    progression[missing_elem_index] = '..'
    question = ' '.join(str(x) for x in progression)

    return [question, answer]
