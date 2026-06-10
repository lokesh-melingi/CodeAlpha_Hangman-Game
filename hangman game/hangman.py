import random

# List of predefined words
words = ["apple", "tiger", "house", "python", "school"]

# Choose a random word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player has guessed the word
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_wrong_guesses - wrong_guesses)

# If player loses
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The correct word was:", word)