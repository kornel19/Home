### Excercise 1.2 | Shoemaker (approx. 1 hours)
# Ask the user to provide a number of days of the week (Monday=1, Sunday=7) when he left his shoes at the
# shoemaker shop for a repair. Ask him also how many days the repair will take. As an output, inform the user at
# which day of the week he should get back his shoes. For example, leaving shoes on Tuesday with 3 days needed for the repair,
# should output Friday



shoes_left = int(input('When you left your shoes at the shoemaker? (Monday=1, Sunday=7): '))
repair_time = int(input('What is the waiting time for repair in days?: '))
pickup = shoes_left + repair_time / 7


if pickup >= 0.14:
    print('You should pickup your shoes on Monday')
elif pickup >= 0.28:
    print('You should pickup your shoes on Tuesday')
elif pickup >= 0.42:
    print('You should pickup your shoes on Wednesday')
elif pickup >= 0.57:
    print('You should pickup your shoes on Thursday')
elif pickup >= 0.71:
    print('You should pickup your shoes on Friday')
elif pickup >= 0.85:
    print('You should pickup your shoes on Saturday')
elif pickup >= 0:
    print('You should pickup your shoes on Sunday')
