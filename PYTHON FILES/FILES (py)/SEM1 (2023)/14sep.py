'''import random
print(random.random())

print(random.randint(1,3))# striding is not available takes start, end
print(random.randrange(4,8,2))

l = [2,345,56,'cfdvf',3.4]





print(random.choice(l))    # no dictionary

random.shuffle(l)  # shuffle not on tuple/ dict
print(l)

d = {12:34, 45:324, 45:34, 34:23,'dv':3}
print(d)


random.seed(1)
print(random.randrange(3,6,1))'''
'''

import random
a = random.randrange(1,6)
print(a)
b = random.uniform(2,8)
print(b)

#uniform gives float value between arguments lower limit not included


'''
'''
#METHOD 1
x = int(input('enter the number : '))
i = 1
sum = 0

for j in range(x-1):
    if x % i == 0:
        sum += i
    i += 1
print(sum)
if sum == x:
    print('IT IS A  PERFECT NUMBER')
else:
    print('NOT A PERFECT NUMBER')


''''''
#METHOD 2

while True:
    x = int(input('Enter Number : '))
    sum = 0

    for i in range(1,x):
        if x % i == 0:
            sum += i

    if x == sum:
        print('THE NUMBER IS PERFECT')

    else:
        print('NOT PERFECT')


'''




'''

x = int(input('Enter number'))

while True:
    if x != int:
        x = int(input('fev'))
''''''

def add():
    ''''''dvdvdbdb'''''''
    print(3)


print(add.__doc__)


'''

def add():
    print(5)
    return(4)

a = add()
print(a)