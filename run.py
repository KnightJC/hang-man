import random

"""
Choices of words for hangman
"""

def pick_word():
    word_list = ["hangman", "python", "programming", "computer", "game", "player"]
    return random.choice(word_list)
