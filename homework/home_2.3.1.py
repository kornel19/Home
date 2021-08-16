#without functions

number = None
list = []

while number != 'STOP':
    number = input('Provide a number: ')
    print('Provide another number or STOP: ')
    if number == 'STOP':
        length = 0
        sum = 0
        average = 0
        maximum = list[0]
        minimum = list[0]
        for i in list:
            length += 1
            sum += i
            if i > maximum:
                maximum = i
            if i < minimum:
                minimum = i
        average = sum / length
        print(f'Number of elements: {length}')
        print(f'Sum of elements: {sum}')
        print(f'Average of elements: {average:.2f}')
        print(f'Max of elements: {maximum}')
        print(f'Min of elements: {minimum}')
    else:
        list.append(int(number))