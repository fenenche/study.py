print("===== WORD GUESS GAME =====")

secret_word = "python"
chances = 3

for attempt in range(chances):
    guess = input("Guess the word: ")

    if guess == secret_word:
        print("Correct! You guessed the word!")
        break
    else:
        print("Wrong guess!")