# how we can break a loop?

while True:
    number = int(input('Provide a number: '))
    print(f'Your number is {number}')

    if number % 2 == 0:
        print('Yey, ending the loop')
        break

print('outside of the while loop')
