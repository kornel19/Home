"""
Write a program that will check the age of the person
based on their year of birth.

Sample program output:
Enter year of birth: 1980
You are of legal age!
"""

year_of_birth = int(input('Provide your year of birth: '))
age = 2021 - year_of_birth

if age >= 18:
    print('You are of a legal age. Grab a beer!')
else:
    print('You are a minor. Some sweets for ya!')

print('Thank you for cooperation. Good bye!')  # watch out for indention!!!

# in Java we would write
# if (age >= 18) {
#     print('You are of a legal age. Grab a beer!');
# } else {
#     print('You are a minor. Some sweets for ya!');
# }
#
# print('Thank you for cooperation. Good bye!')  # watch out for indention!!!