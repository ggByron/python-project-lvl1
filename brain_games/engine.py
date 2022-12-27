#!/usr/bin/env python3
from random import randint
import prompt


def get_username():
    username = prompt.string('May I have your name? ')
    return username
     
def generate_number():
    return randint(1, 100)


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return 'Correct!'
    

def play_game(game):
    print('Welcome to the Brain Games!')
    username = get_username()
    print(f'Hello, {username}!')
    print(game.DESCRIPTION)
    correct_answers = 0
    while correct_answers < 3:
        question = game.make_question()
        print(question)
        user_answer = game.get_user_answer()
        correct_answer = game.correct_answer(int(question[-2:]))
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again, {username}!")
            quit()
    print(f'Congratulations, {username}!')

