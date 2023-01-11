import prompt
ROUNDS_COUNT = 3


def play(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game.DESCRIPTION)
    for _ in range(0, ROUNDS_COUNT):
        question, answer = game.make_qstn_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string()
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f"Correct answer was {answer}."
                  f"\nLet's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')
