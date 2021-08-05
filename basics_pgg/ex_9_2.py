"""
Write a program that will calculate the result of the given operation
(adding, subtracting, multiplying, dividing) based on the two numbers given.
If an incorrect operation is specified, the program should
display an appropriate error message.

Sample program output:
Enter the first number: 10
Enter the second number: 5
Enter the type of operation (+, -, *, /): +
Result: 15
"""

number_1 = float(input('Enter the first number: '))
number_1 = round(number_1, 2)
print(number_1)

number_2 = float(input('Enter the second number: '))
number_2 = round(number_2, 2)
print(number_2)
operation = input('Enter the type of operation (+, -, *, /): ')

if operation == '+':
    print(round(number_1 + number_2, 2))
elif operation == '-':
    print(round(number_1 - number_2, 2))
elif operation == '*':
    print(round(number_1 * number_2, 2))
elif operation == '/':
    print(round(number_1 / number_2, 2))
else:
    print('invalid operator')
