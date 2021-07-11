# This function chooses from a random word from a list of words and then runs a code
# which demonstrates a hangman game. 

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
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = ''
    for i in secretWord:
        if i in lettersGuessed:
            s += i
        else:
            s +='_ '
    return s




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s = ''
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in lettersGuessed:
            s+= i
    return s
    

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
    n = len(secretWord)
    print ('Welcome to the game Hangman!')
    print ('I am thinking of a word that is '+str(n)+' letters long.')
    print ('------------')
    count = 6
    
    lettersGuessed = []
    while count>0:
        if isWordGuessed(secretWord, lettersGuessed):
            print ('Congratulations, you won!')
            break
        print('you have '+str(count)+' guesses left.')
        s = getAvailableLetters(lettersGuessed)
        print ('Available letters: '+ s)
        x = input('Please guess a letter: ')
        if x not in secretWord:
            if x in lettersGuessed:
                count += 1
                print ("Oops! You've already guessed that letter: "+ str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                lettersGuessed.append(x)
                print ('Oops! That letter is not in my word:' + str(getGuessedWord(secretWord, lettersGuessed)))
        else:
          count += 1
          if x not in lettersGuessed:
              lettersGuessed.append(x)
              print ('Good guess: '+ str(getGuessedWord(secretWord, lettersGuessed)))
             
          else:
              print ("Oops! You've already guessed that letter: "+ str(getGuessedWord(secretWord, lettersGuessed)))
        print ('------------')
        count -=1
    if count == 0:
        print ('Sorry, you ran out of guesses. The word was '+ secretWord + '.')



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
