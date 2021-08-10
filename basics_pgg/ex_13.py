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