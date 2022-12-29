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
      
    missing_element = randint(1, 8)
    progression[missing_element] = '..' 
    
    return progression
    

def correct_answer(question):
    missing_element = question.index('..')
    answer = (question[missing_element - 1] + question[missing_element + 1]) / 2
    return str(int(answer))