"""
Write a program that will check the age of the person
based on their year of birth.

Sample program output:
Enter year of birth: 1980
You are of legal age!
"""

import datetime

year_of_birth = int(input('Provide your year of birth: '))
current_year = datetime.datetime.now().year
print(current_year)
age = current_year - year_of_birth

if age >= 18:
    print('You are of a legal age. Grab a beer!')
else:
    print('You are a minor. Some sweets for ya!')

print('Thank you for cooperation. Good bye!')  # watch out for indention!!!
