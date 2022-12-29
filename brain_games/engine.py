#!/usr/bin/env python3
from random import randint
import prompt


def get_username():
    username = prompt.string('May I have your name? ')
    return username


def generate_number():
    return randint(1, 25)


def get_user_answer():
    user_answer = prompt.string()
    return user_answer


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
        user_answer = get_user_answer()
        correct_answer = game.correct_answer(question)
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}."
                  f"\nLet's try again, {username}!")
            quit()
    print(f'Congratulations, {username}!')
