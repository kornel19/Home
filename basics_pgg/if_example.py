# conditional statement

number = int(input('Provide a number: '))

print('before if')

if number == 10:
    print('Congrats! You won!')
elif number == 20:
    print('Nice! 20 is ok as well :)')
elif number == 30:
    print('Huge prize for you!')
else:
    print('Oh no! No prize this time! Try again :(')


print('after if')
