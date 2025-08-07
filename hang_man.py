import random

# A list of words to choose from
word_list = ["python", "hangman", "programming", "computer", "challenge", "developer"]
secret_word = random.choice(word_list).upper()
display_word = ["_" for _ in secret_word]
lives = 6
guessed_letters = []

print("Welcome to Hangman! Guess the word.")
# This is an ASCII art representation of the hangman figure
# You can customize this to be more elaborate
hangman_art = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    """
]

while lives > 0 and "_" in display_word:
    print(hangman_art[6 - lives])  # Display the hangman based on lives remaining
    print(" ".join(display_word))
    print(f"Lives remaining: {lives}")

    guess = input("Guess a letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("Correct guess! 🎉")
    else:
        lives -= 1
        print("Incorrect guess. 😬")

# End of game logic
if "_" not in display_word:
    print(f"\nCongratulations! You guessed the word: {secret_word}!")
else:
    print(hangman_art[6])
    print(f"\nGame over! The word was: {secret_word}. 💀")