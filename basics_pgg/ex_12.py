"""
Write a program that calculates the average temperature
for a given week based on temperatures entered by the user.
"""

day_number = 1
temperature_sum = 0

while day_number <= 7:
    temperature_sum += int(input(f'Provide temp for day {day_number}: '))
    print(temperature_sum)
    day_number += 1

# calculate the average temperature
average_temperature = temperature_sum / 7

# print the results
print(f'Average temperature for this week is {average_temperature:.2f}')
