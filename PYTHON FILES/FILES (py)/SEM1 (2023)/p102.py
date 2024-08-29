a = 'n'
while a == 'n':
    a = input('enter n or y')
    if a != 'y' or a != 'n':
        while True:
            a = input('only y or n')
    else:
            break