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
    Adding letters to be guessed as well as an invalid input if entered incorrectly
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
            |      O
            |     \|/
            |      |
            |     / \
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
            |      |
            |      |
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
            |
            |
            |
            |
            -
        '''
    ]
    return stages[6 - attempts] 
