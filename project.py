import random

def select_word():
    words = ["apple", "banana", "cherry", "date", "grape"]
    return random.choice(words)

def get_hangman_stage(remaining_attempts):
    stages = [
        """
        ------
        |    |
        |
        |
        |
        |
        |__________
        """,
        """
        ------
        |    |
        |    O
        |
        |
        |
        |__________
        """,
        """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |__________
        """,
        """
        ------
        |    |
        |    O
        |   /|
        |    |
        |
        |__________
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |    |
        |
        |__________
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |    |
        |   /
        |__________
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |    |
        |   / \\
        |__________
        """
    ]
    return stages[6 - remaining_attempts]

def print_secret_word(secret_word, guessed_letters):
    print(" ".join([letter if letter in guessed_letters else "_" for letter in secret_word]))
    print("\n")

def hangman():
    secret_word = select_word()
    guessed_letters = set()
    remaining_attempts = 6

    print("Welcome to Hangman! Let's see if you can guess this word!\n")
    print(get_hangman_stage(remaining_attempts))
    print_secret_word(secret_word, guessed_letters)

    while remaining_attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You have already guessed the letter '{guess}'")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Yes! The letter '{guess}' is part of the secret word.")
        else:
            print(f"No! The letter '{guess}' is not part of the secret word.")
            remaining_attempts -= 1

        print(get_hangman_stage(remaining_attempts))
        print_secret_word(secret_word, guessed_letters)
        print(f"\n{remaining_attempts} attempts remaining\n")

        if all(letter in guessed_letters for letter in secret_word):
            print("+++ Well done, you have won this game! +++\n")
            return

    print("--- Sorry, you have lost this game! ---\n")
    print(f"The secret word was: {secret_word}\n")

if __name__ == "__main__":
    hangman()
