"""
Using variable assignment, write a program to calculate
the trapezoid field with base lengths 3 and 9 and height 6.5.
formula = 1/2*(base1+base2)*height
"""

# PEP - Python Enhancements Proposal
# PEP8 - Style guide https://www.python.org/dev/peps/pep-0008
# Naming convention https://realpython.com/python-pep8/#naming-conventions

short_base = 3
long_base = 9
height = 6.5
area = 1 / 2 * (short_base + long_base) * height

print(area)
print(short_base, long_base, height, area)
