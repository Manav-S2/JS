c = 'n'
while True:
    if c == 'n':
        c = input('press y or n')
        if (c != 'y' or c != 'n'):
            c = input('press just y or n')
        else:
            break