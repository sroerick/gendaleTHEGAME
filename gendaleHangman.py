import random 
HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
=============''', '''

   +---+
   |   | 
   O   |
       |
       |
       |
============''', '''

   +---+
   |   | 
   O   |
   |   | 
       |
       |
============''', '''

   +---+
   |   |
   O   | 
  /|   |
       |
       |
============''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
============''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
===========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
===========''']
words = 'monarch mkultra brainwash flashing kanye dronestrike assassination drill preparedness homeland deaths police antichrist lucifer gendale corporeality plague virus smallpox ebola airplane greyhound cartel narco marijuana zetas alquaeda afghanistan iraq nuclear katrina lilwayne betsy kennedy ufo alien'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex] 

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)]) 
    print() 
   
    print('Missed letters:', end=' ') 
    for letter in missedLetters: 
        print(letter, end=' ') 
    print() 

    blanks = '_' * len(secretWord) 
    
    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters: 
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:] 
    for letter in blanks: # show the secret word with spaces in between each letter 
        print(letter, end=' ') 
    print() 
def getGuess(alreadyGuessed): 
    while True: 
        print('Guess a letter.') 
        guess = input() 
        guess = guess.lower() 
        if len(guess) != 1: 
            print('Please enter a single letter.') 
        elif guess in alreadyGuessed: 
            print('You have already guessed that letter. Choose again.') 
        elif guess not in 'abcdefghijklmnopqrstuvwxyz': 
            print('Please enter a LETTER.') 
        else: 
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    guess = getGuess (missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! the secret word is "' + secretWord + '"! You have won!')
            gameIsDone = true
    else:
        missedLetters = missedLetters + guess

        #check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = '' 
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break 
