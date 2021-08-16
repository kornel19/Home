## 1. Interaction with the user
### Excercise 1.1 | Interaction with the user and simple calculations (approx. 2 hours)
## Ask user (using `input()` function) to provide the number of kilograms of potatoes he'd like to buy and how much
# 1-kilogram costs. The program should display how much user have to pay.

weight = float(input('Provide the number of kg of potatoes: '))
price = float(input('Provide the cost of 1 kg: '))
to_pay = weight * price

print('You have to pay ' + str(to_pay))
