import random

"""
Choices of words for hangman
"""


def pick_word():
    word_list = ["hangman", "python", "programming", "computer", "game", "player"]
    return random.choice(word_list)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()
    

    """
    Adding letters to be guessed as well as an invalid
    input if entered incorrectly
    """


def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single letter.")

    """
    Adding ASCII art for better visual experience as well as attempts made
    """


def draw_hangman(attempts):
    stages = [
        '''
            --------
            |      |
            |
            |
            |
            |
            -
        ''',
        '''
            --------
            |      |
            |      O
            |
            |
            |
            -
        ''',
        '''
            --------
            |      |
            |      O
            |      |
            |      |
            |
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \|
            |      |
            |
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \|/
            |      |
            |
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \|/
            |      |
            |     /
            -
        ''',
        '''
           --------
            |      |
            |      O
            |     \|/
            |      |
            |     / \
            -
        '''
    ]
    return stages[6 - attempts]


"""
adding words picked, correct, incorrect and attemps
"""


def play_game():
    while True:
        word = pick_word()
        guessed_letters = []
        incorrect_guesses = []
        attempts = 6

        print("Welcome to Hangman!")
        print("The word has", len(word), "letters.")

        while True:
            print(draw_hangman(attempts))
            print("Attempts left:", attempts)
            print("Word:", display_word(word, guessed_letters))
            print("Incorrect guesses:", " ".join(incorrect_guesses))

            if "_" not in display_word(word, guessed_letters):
                print("Congratulations! You guessed the word correctly!")
                break

            guess = get_guess()

            if guess in guessed_letters or guess in incorrect_guesses:
                print("You already guessed that letter. Try again.")
                continue

            if guess in word:
                guessed_letters.append(guess)
                print("Correct guess!")
            else:
                incorrect_guesses.append(guess)
                attempts -= 1
                print("Incorrect guess.")

                if attempts == 0:
                    print("Sorry, you ran out of attempts. The word was:", word)
                    break

        """
        Added end game loop to play again or exit game
        """

        play_again = input("Do you want to play again? (yes/no): ").lower()
        
        while play_again != "yes" and play_again != "no":
            play_again = input("Invalid input. Please enter 'yes' or 'no': ")
        
        if play_again == "no":
            break

    print("Thanks for playing!")

play_game()
