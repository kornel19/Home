### Excercise 1.7 | Counting prices (approx. 0,5 hours)
#Ask a user for a product he'd like to byt, its quantity and price. Based on that display a proper information.
#Example:
#What would you like to buy? - tomatoes
#Provide a price - 5
#Provide quantity - 10
#For tomatoes, you'd like to buy, you have to pay 50 PLN.

product= input('What would you like to buy?: ')
price = float(input('Provide a price: '))
quantity= int(input('Provide quantity: '))
calculation= price*quantity

print(f'For {product} you would like to buy, you have to pay {calculation:.2f} PLN')
