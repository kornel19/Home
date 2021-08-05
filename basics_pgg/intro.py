
# this is comment
# f(x) = x + 2
# f(5) -> 5 + 2 -> 7
print("Hello world!")
print(2 + 2)

# Data types

# string - str
print("Hello world!")
print('Hello world!')

# print(Hello world) - this will not work, will cause SyntaxError

# integers - int
print(10)
print(-5)

# float
print(3.14)
print(-10.5)
print(3.0)

# bool
print(True)
print(False)

# None -> value that represent the lack of value
# empty value
# null -> in other programming languages

print(type(10))  # int
print(type(10.0))  # float
print(type("10"))  # str

# Operators
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 % 3)
print(10 ** 3)
print("I see " + "the cat")
print("-" * 10)

# variables
first_name = "Piotr"
print(first_name)
first_name = 'Tom'
print(first_name)


print('-'*60)

# Comparison operators
# always return bool value -> True/False
print(1 == 1)  # equality operator: ==  whereas = is assignment operator
print(1 != 1)
print(1 > 1)
print(1 < 1)
print(1 >= 1)
print(1 <= 1)

# Assignment operators
print('-'*30)
number = 10
# number + 5 -> this will not change the value in variable number
number = number + 5
number += 5
number += 1
number -= 1
number *= 5
number /= 10
number **= 2
print(number)

# Logical operators
print('-'*30)
print(True and True)
print(False or True)
print(not False)
print( (True and False) or (False or True) )
print( False or True )
print( True )
