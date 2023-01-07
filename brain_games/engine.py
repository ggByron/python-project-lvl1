import prompt


def play_game(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game.DESCRIPTION)
    for n in range(0, 3):
        question = game.make_question()
        print(question)
        user_answer = prompt.string()
        correct_answer = game.correct_answer(question)
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}."
                  f"\nLet's try again, {username}!")
            quit()
    print(f'Congratulations, {username}!')
