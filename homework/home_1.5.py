"""
Excercise 1.5 | Triangle area (approx. 1 hours)
Write a program that will ask a user for the lengths of the sides of a triangle. Check if it's possible to create
a triangle from those lengths and if so, calculate the area of the triangle.
To calucate squre root use:
import math
x = math.sqrt(10)
"""
import math
from math import sqrt

a = float(input('Provide side a: '))
b = float(input('Provide side b: '))
c = float(input('Provide side c: '))
p= (a + b + c) /2

if (a+b>c) and (b+c>a) and (a+c>a):
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'You can build a triangle and its area is {area:.2f}')
else:
    print('I\'m sorry, but you can\'t build a triangle with these sides')






