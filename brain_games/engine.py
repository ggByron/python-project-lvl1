import prompt


def play(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game.DESCRIPTION)
    ROUNDS = 3
    for _ in range(0, ROUNDS):
        question, answer = game.make_qstn_and_answer()
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
