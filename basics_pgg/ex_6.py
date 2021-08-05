"""
Write a program to check if the number given by the user:
is odd, divisible by 3 and greater than 10
or
is the number 7
"""

number = int(input('Provide a number: '))

result = (number % 2 != 0 and number % 3 == 0 and number > 10) or number == 7

print(f'Result: {result}')
