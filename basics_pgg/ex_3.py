"""
Write a program calculating the amount due for the purchased goods
based on the price per kilogram and the number of kilograms purchased.
Use variables to store price and weight. Write all information to the console.

Sample program output:
Price per kg: 10.0
Weight: 2.5
Total price: 25.0
"""

# input returns string (not a number) and we have to convert string
# to float, so we can make mathematical operations with mathematical operators like *
price = float(input('Provide price per kg: '))
weight = float(input('Provide weight: '))
print(type(price), type(weight))
total_price = price * weight

# 1 method
print('Price per kg: ' + str(price))
print('Weight: ' + str(weight))
print('Total price: ' + str(total_price))

# 2 method
print('Price per kg:', price)
print('Weight:', weight)
print('Total price:', total_price)

# 3 method
# f-strings, formatted strings
print(f'Price per kg: {price}')
print(f'Weight: {weight}')

# format specifiers
# https://www.python.org/dev/peps/pep-0498/#format-specifiers
# https://docs.python.org/3.9/library/string.html#formatspec
print(f'Total price: {total_price:_<10.2f}')

