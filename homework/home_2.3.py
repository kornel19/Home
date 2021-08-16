"""
Write a program that will read numbers from the user, use `STOP` as a command to stop reading numbers.
Then, display the following stats:
- number of provided numbers, how many
- sum,
- average,
- minimum
- maximum

In one version use build-in functions in the other not.
"""
from statistics import mean

number = None
list = []

while number != 'STOP':
    number = input('Provide a number: ')
    print('Provide another number or STOP: ')
    if number == 'STOP':
        print(f'Number of elements: {len(list)}')
        print(f'Sum of elements: {sum(list)}')
        print(f'Average of elements: {mean(list):.2f}')
        print(f'Max of elements: {max(list)}')
        print(f'Min of elements: {min(list)}')
    else:
        list.append(int(number))



