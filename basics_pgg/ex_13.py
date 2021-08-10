"""
Write a program displaying the minimum and maximum number of all numbers entered by the user.
Give the user the ability to finish entering numbers with the appropriate command (STOP for example).
Make sure the case where the user does not enter any number works properly.

How we can do that?
- let's define two variables where we can store minimum and maximum values from the provided numbers
- at the beginnig we will assign None to those variables
- we will use infinite WHILE loop for getting data from the user.
    - IF user will provide "STOP" value, then we will stop the loop
    - ELSE
        - check the existing value in minimum/maximum variable - if None, assign a value from the user
        - check the provided number if greater than maximum or lower than minimum and then properly assign new value
"""

minimum = None
maximum = None

while True:
    input_data = input('Provide a number or STOP: ')

    # if input_data equals STOP break the loop
    if input_data == 'STOP':
        break  # breaks the loop, no code from the loop will be executed after break is fired

    # convert input_data to int
    try:
        number = int(input_data)
    except ValueError:
        print('The number you have provided is invalid')
        continue

    # if minimum is None or provided number is less than minimum assign this value to minimum
    if minimum is None or number < minimum:
        minimum = number

    # do the same with maximum
    if maximum is None or number > maximum:
        maximum = number

# after the loop present results
if minimum is None or maximum is None:
    print('You didn\'t provided any numbers.')
else:
    print(f'Provided minimum = {minimum}, maximum = {maximum}')
