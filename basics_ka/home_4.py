### Excercise 1.4 | Hotel fee (approx. 1,5 hours)
# Write a program, where the user provides his age and the number of nights he wants to stay at the hotel.
# Based on that values calculate the fee for his stay. The rules are:
# - minor (below 18 years old) will pay 100 PLN per night
#- adults (of age 18 but less than 65) will pay:
#    - 200 PLN if they are staying for one night
#    - 180 PLN if they are staying for at least 2 nights but less than 5
#    - 150 PLN if they are staying for 5 and more nights
# - pensioners (65 and older) will pay the same rate as adults but with a 10% discount
# For example, if a user is 70 years old and will spend 10 nights at the hotel, he will pay 150 PLN - 10% discount = 135 PLN per night,
# so for the whole stay, he will pay 1350 PLN.

age = int(input('Provide your age: '))
nights= int(input('How many nights you want to stay at the hotel?: '))
cost_1 = 100
cost_2 = 200
cost_3 = 180
cost_4 = 150

if age < 18:
    print(f'Fee {cost_1 * nights}')
elif age >= 18 and age < 65 and nights < 2:
    print(f'Fee {cost_2 * nights}')
elif age >= 18 and age < 65 and nights >= 2 and nights < 5:
    print(f'Fee {cost_3 * nights}')
elif age >= 18 and age < 65 and nights >= 5:
    print(f'Fee {cost_4 * nights}')
elif age >= 65 and nights < 2:
    print(f'Fee {cost_2 * nights - (night* cost_2 * 0.1)}')
elif age >= 65 and nights >= 2 and nights < 5:
    print(f'Fee {cost_ * nights - (nights * cost_3 * 0.1)}')
elif age >= 65 and nights >= 5:
    print(f'Fee {cost_4 * nights - (nights * cost_4 * 0.1)}')





