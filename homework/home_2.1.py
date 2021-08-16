"""
Write a program that will draw two numbers from the range from 0 do 99. Display those numbers and ask the user what is the
sum of them (do not display the result). Ask user for a correct answer till he provides a correct one.
"""

from random import randint

number_1 = randint(0, 99)
number_2 = randint(0, 99)
sum = (number_1 + number_2)
print(f'Your numbers are {number_1} and {number_2}, what is the sum of them ?')
answer= int(input('The sum is equal to: '))

while answer != sum:
    print('Try to recalculate')
    answer = int(input('The sum is equal to: '))

print('Congratulations, you answered correctly')


