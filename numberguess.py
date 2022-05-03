#quick program to have user guess a number

from random import randint

random_num = randint(1,10)

user_num = input('Please enter a number between 1 and 10: ')

if user_num == random_num:
    print('YOU WIN')
else:
    print('You lose :(')