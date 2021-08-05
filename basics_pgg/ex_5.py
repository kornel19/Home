"""
Write a program to check if the number given by the user is:
- greater than 10
- less than 15
- divisible by 2 (use the modulo operator)

Sample program output:
Enter the number: 15

Greater than 10: True
Less than 15: False
Divisible by 2: False
"""

number = int(input('Provide a number: '))

print(f'Greater than 10: {number > 10}')
print(f'Less than 15: {number < 15}')
print(f'Disivible by 2: {number%2 == 0}')
