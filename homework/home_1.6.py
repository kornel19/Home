#Assumptions:
 #   - 0-6   - kindergarten - ticket price: 0
  #  - 7-17  - school       - ticket price: 2.28
   # - 18-64 - adult        - ticket price: 3.80
    #- +65   - pensioner    - ticket price: 1.90
#Write a program that will ask a user for his age and a number of tickets he'd like to buy.
#Based on the assumptions above calculate the price he should pay for the tickets.


age = int(input('Provide your age: '))
number= int(input('How many tickets you want to buy? '))
kindergarten = 0
school = 2.28
adult = 3.80
pensioner = 1.90

if age >= 0 and age < 7:
    print(f'You should buy kindergarten ticket. The total price is {kindergarten * number:.2f}')
elif age >= 7 and age < 18:
    print(f'You should buy school ticket. The total price is {school * number:.2f}')
elif age >= 18 and age < 65:
    print(f'You should buy adult ticket. The total price is {adult * number:.2f}')
elif age >= 65:
    print(f'You should buy pensioner ticket. The total price is {pensioner * number:.2f}')