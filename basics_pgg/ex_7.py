"""
Write a program that, based on the dimensions of the packaging,
calculates its volume and checks whether it is larger than 1 liter (1000 cm3).

x =
y =
z =
"""

x = int(input('Provide x: '))
y = int(input('Provide y: '))
z = int(input('Provide z: '))

# calculations
volume = x * y * z
bigger_than_liter = volume > 1000

# output
print(f'Volume: {volume}')
print(f'Bigger than liter? {bigger_than_liter}')