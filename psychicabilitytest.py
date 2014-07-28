# This is a program to test the users psychic ability
import random

failedPsync = 0

print("Hello! What is your corporation?")
CorpUS = input()

truth = random.randint(1,20)
print('ATTN ' + CorpUS + '! We are thinking of a number between 1 and 20')

while failedPsync < 3:
	print('Take a guess.') 
	psync = input()
	psync = int(psync)

	failedPsync = failedPsync + 1

	if psync < truth:
		print('Your psychic powers are trending low')

	if psync > truth:
		print('Your psychic powers are trending high')

	if psync == truth: 
		break

if psync == truth:
	failedPsync = str(failedPsync)
	print('Well done. You have proved your psychic powers and brought glory to your masters at ' + CorpUS + 'in only ' + failedPsync + ' guesses!')


if psync != truth:
	truth = str(truth)
	print('You are not psychic and have brought shame to ' + CorpUS + '! You are not fit to work!')
