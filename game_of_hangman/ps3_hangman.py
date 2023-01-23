# Hangman game


import random

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


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    x = []

    for i in secretWord:
        if i in lettersGuessed:
            x.append(i)
     
    return len(x) == len(secretWord)
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    x = ''
    for i in secretWord:
        if i in lettersGuessed:
            x += i + ' '
        else:
            x += '_ '
    
    return x


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    x = list(string.ascii_lowercase)
    for i in lettersGuessed:
       if i in x:
           x.remove(i)
       
    x = ''.join(x)
    return x
    

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
    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    n = 0
    lettersGuessed = []
    print('-----------')
    while n < 8:
        print('You have ' + str(8 - n)+ ' guesses left.')
        print('Available letters: ', getAvailableLetters(lettersGuessed))
        k = input('Please guess a letter: ')
        k = k.lower()
        if k in list(secretWord) and k not in lettersGuessed:
            lettersGuessed.append(k)
            print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
        elif len(lettersGuessed) != 0 and k in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        elif k not in list(secretWord):
            lettersGuessed.append(k)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            n += 1
        print('-----------')
        if '_' not in getGuessedWord(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
    if '_' in getGuessedWord(secretWord, lettersGuessed):
            print('Sorry, you ran out of guesses. The word was', secretWord, '.')   
    return 



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
