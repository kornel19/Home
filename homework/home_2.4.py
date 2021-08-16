"""
Write a program that will draw a number from a range from 0 to 999. The users task is to guess that number.
When the user provides wrong number, give him a hint, whether the number he is looking for is bigger or smaller
from the one he gave.
"""

from random import randint

number = randint (0, 999)

user_number = int(input('Guess a number from 0 - 999: '))

while user_number != number:
    if user_number < number:
        print('The number is bigger')
    elif user_number > number:
        print('The number is smaller')
    user_number = int(input('Try again: '))
print('Congratulations, you answered correctly')
