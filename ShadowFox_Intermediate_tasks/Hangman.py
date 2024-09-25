import random

HANGMAN_PICS = ['''
      +---+
      |
      |
      |
     ===''', '''
 	  +---+
      |   O
      |
      |
     ===''', '''
      +---+
      |   O
      |   |
      |
     ===''', '''
      +---+
      |   O
      |  /|
      |
     ===''', '''
      +---+
      |   O
      |  /|\\
      |
     ===''', '''
      +---+
      |   O
      |  /|\\ 
      |  /
     ===''', '''
      +---+
      |   O
      |  /|\\
      |  / \\
     ===''']

# Words with hints
words_with_hints = {
    'python': 'A popular programming language.',
    'cricket': 'A popular sport in India.',
    'lion': 'The King of Animals.',
    'sachin': 'The God of Cricket.',
    'pacific': 'The largest ocean in the World.',
    'asia':'The largest continent in the World.',
    'ronaldo':'Popular Football player in the world.',
    'thor' : 'The god of Thunder',
}

def get_random_word_and_hint(word_dict):
    """Selects a random word and its hint from the dictionary."""
    word = random.choice(list(word_dict.keys()))
    return word, word_dict[word]

def display_game_state(HANGMAN_PICS, wrong_guesses, correct_guesses, secret_word):
    #Displays the current state of the game, including the hangman and word progress.
    print("****************************")
    print(HANGMAN_PICS[len(wrong_guesses)])
    print("****************************")
    print("\nWrong guesses: ", " ".join(wrong_guesses))
    word_progress = [letter if letter in correct_guesses else '_' for letter in secret_word]
    print("\nWord: ", " ".join(word_progress))

def play_hangman():
    secret_word, hint = get_random_word_and_hint(words_with_hints)
    wrong_guesses = []
    correct_guesses = []
    max_guesses = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")
    print(f"Hint: {hint}\n")

    while True:
        display_game_state(HANGMAN_PICS, wrong_guesses, correct_guesses, secret_word)
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in correct_guesses or guess in wrong_guesses:
            print("You've already guessed that letter.")
            continue

        if guess in secret_word:
            correct_guesses.append(guess)
            if all(letter in correct_guesses for letter in secret_word):
                print(f"\nCongratulations! You've guessed the word '{secret_word}' correctly!")
                break
        else:
            wrong_guesses.append(guess)
            if len(wrong_guesses) == max_guesses:
                display_game_state(HANGMAN_PICS, wrong_guesses, correct_guesses, secret_word)
                print(f"\nYou've run out of guesses! The word was '{secret_word}'.")
                break

if __name__ == "__main__":
    play_hangman()
