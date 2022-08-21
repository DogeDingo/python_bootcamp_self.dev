# first of all we know that we want to choose randomly from the list
# which means we have to import the library random
import random
import string

from words_for_hangman import words_for_hangman

def get_valid_word(words_for_hangman):
    word = random.choice(words_for_hangman) #randomly chooses something from the list
    while '-' in words_for_hangman or ' ' in words_for_hangman:
        random.choice(words_for_hangman) # while there is a dash or a space in the randomly chosen word
                                        # go through the while loop again
    return word.upper()

def hangman():
    word = get_valid_word(words_for_hangman)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase) # import an alphabet from the english language
    used_letters = set() # what the user has guessed

user_input = input('Type something')
