"""
Write a program that calculates the square
of the first 100 natural numbers
and prints the results to the console.

Sample program output:
...
10 square equals 100
...
"""

# 2**2 = 4

i = 1
while i <= 100:
    print(f'{i} square equals {i ** 2}')
    i += 1  # equivalent of i = i + 1, there is no i++ in python
