import random
import time

def openingCredits():
    print('You find yourself sitting at a computer console.')
    print('A prompt flashes, reminding you it is GENDALE which makes this happen')
    print('You create a front organization, and are then asked what you want to do')
    print('You decide to learn how to program.')
    print('You study the source code and all the comments and jokes therein')
    time.sleep(2)
    print('You are grateful having been tought how to program')
    input('press enter to be grateful')

def chooseLife():
    life = ''
    while life != '1' and life != '2':
        print('You are given the option to join a technology company. Do you pick company 1 or 2?')
        life = input()

    return life


def ventureCapital (chosenLife):
    print('You work hard at your new job') 
    time.sleep(2)
    print('You launch innovative features and develop a loyal following.')
    time.sleep(2)
    print('Your firm begins getting offers from ventureCapital firms')
    print()
    time.sleep(2)

    trueBeliever = random.randint(1,2)

    if chosenLife == str(trueBeliever):
        print('Your boss turns down the offers. You make an amazing product and history.')
    else:
        print('Your boss accepts the offers. Now you work for Satan!')

endlessCycle = 'yes'
while endlessCycle == 'yes' or endlessCycle == 'y':

    openingCredits()
  
    lifeNumber = chooseLife()

    ventureCapital(lifeNumber)

    print('reincarnate? (yes or no)')
    endlessCycle = input()

   
  
