import random

numlist = [0, 1, 2, 3, 4, 5]

numright = random.choice(numlist)

numchoice = int(input('Guess a number from 0 to 5: '))

if numright == numchoice:
    print('Congrats! You guesse the right number: {}!'.format(numright))
else:
    print('Wrong!')
    while numchoice != numright:
        numchoice = int(input('Try again: Guesse a number from 0 to 5: '))
    if numright == numchoice:
        print('You guessed the number {}!'.format(numright))
