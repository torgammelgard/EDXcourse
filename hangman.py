"""Loading word list from file...
	55900 words loaded.
	Welcome to the game Hangman!
	I am thinking of a word that is 4 letters long
	-----------
	You have 8 guesses left
	Available Letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Oops! That letter is not in my word: _ _ _ _

	Sorry, you ran out of guesses. The word was else."""

import string


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    res = ''
    for c in secretWord:
        if c in lettersGuessed:
            res += c +' '
        else:
            res += ' _'
    return res

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    res = ''
    for c in string.ascii_lowercase:
        if c not in lettersGuessed:
            res += c
    return res
