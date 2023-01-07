import prompt


def play_game(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game.DESCRIPTION)
    for n in range(0, 3):
        q_and_a = game.make_qstn_and_answer()
        question = q_and_a[0]
        answer = q_and_a[1]
        print(f"Question: {question}")
        user_answer = prompt.string()
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f"Correct answer was {answer}."
                  f"\nLet's try again, {username}!")
            quit()
    print(f'Congratulations, {username}!')
