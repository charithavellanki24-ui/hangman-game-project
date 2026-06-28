import random

# List of 5 predefined words
words = ["python", "java", "apple", "tiger", "house"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print("You have 6 incorrect guesses allowed.\n")

while incorrect_guesses < max_attempts:
    
    # Display current progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check win condition
    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    # Check guessed letter
    if guess in guessed_letters:
        print("You already guessed this letter.")
    
    elif guess in word:
        print("Correct guess!")
        guessed_letters.append(guess)

    else:
        print("Wrong guess!")
        guessed_letters.append(guess)
        incorrect_guesses += 1
        print("Remaining attempts:", max_attempts - incorrect_guesses)

# If attempts finished
if incorrect_guesses == max_attempts:
    print("\nGame Over!")
    print("The word was:", word)