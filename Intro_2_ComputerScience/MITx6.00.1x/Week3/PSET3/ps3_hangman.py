# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
      if letter not in lettersGuessed:
        return False
    
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedLetters = ''

    for letter in secretWord:
      if letter in lettersGuessed:
        guessedLetters += letter
      else:
        guessedLetters += '_ '
    
    return guessedLetters



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ''

    for letter in string.ascii_lowercase:
      if letter not in lettersGuessed:
        availableLetters += letter
    
    return availableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")
    guessesLeft = 8
    lettersGuessed = []
    
    while True:
      print("You have " + str(guessesLeft) + " guesses left.")
      print("Available letters:", getAvailableLetters(lettersGuessed))
      letter = input("Please guess a letter:")

      if letter in lettersGuessed:
        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        print("-------------")
      
      elif letter in secretWord:
        lettersGuessed += letter
        print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        print("-------------")

        if isWordGuessed(secretWord, lettersGuessed):
          print("Congratulations, you won!")
          break

      else:
        print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        print("-------------")
        lettersGuessed += letter
        guessesLeft -= 1
        
        if guessesLeft == 0:
          print("Sorry, you ran out of guesses. The word was", secretWord)
          break







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

# Test Cases isWordGuessed(secretWord, lettersGuessed)
# print(isWordGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's'])) #False
# print(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])) #True
# print(isWordGuessed('coconut', ['v', 'b', 's', 'q', 'i', 'a', 'e', 'g', 'w', 'r'])) #False
# print(isWordGuessed('broccoli', ['v', 't', 'a', 'q', 'o', 'w', 'f', 'z', 's', 'c'])) #False
# print(isWordGuessed('lettuce', [])) #False
# print(isWordGuessed('mangosteen', ['z', 'x', 'q', 'm', 'a', 'n', 'g', 'o', 's', 't', 'e', 'e', 'n'])) #True

# Test Cases getGuessedWord(secretWord, lettersGuessed)
# print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])) #' _ pp _ e'
# print(getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'])) #'durian'
# print(getGuessedWord('banana', ['l', 'v', 'q', 'x', 'o', 'n', 'd', 'h', 'w', 'm'])) #' _  _ n _ n _ '
# print(getGuessedWord('mangosteen', ['d', 'c', 'f', 'i', 'z', 'o', 'p', 'u', 's', 'r'])) #' _  _  _  _ os _  _  _  _ '
# print(getGuessedWord('mangosteen', [])) #' _  _  _  _  _  _  _  _  _  _ '
# print(getGuessedWord('coconut', ['y', 'e', 'l', 'b', 'q', 'f', 's', 't', 'n', 'o'])) #' _ o _ on _ t'

# Test Cases getAvailableLetters(lettersGuessed)
# print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])) #abcdfghjlmnoqtuvwxyz
# print(getAvailableLetters([])) #'abcdefghijklmnopqrstuvwxyz'
# print(getAvailableLetters(['s', 'm', 'u', 'k', 'x', 'd', 't', 'o', 'p', 'i', 'v'])) #'abcefghjlnqrwyz'
# print(getAvailableLetters(['o', 'j', 'w'])) #'abcdefghiklmnpqrstuvxyz'
# print(getAvailableLetters(['c', 'v', 'g', 'i', 'e'])) #'abdfhjklmnopqrstuwxyz'
# print(getAvailableLetters(['v', 't', 'i', 'a', 'q', 'k', 'o', 'x', 'c', 'n', 'm', 'j'])) #'bdefghlprsuwyz'