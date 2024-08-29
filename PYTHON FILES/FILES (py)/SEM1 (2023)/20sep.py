'''def myfunc(a,b):
    global c
    c = a+b
    print(c)
    return c

def mysecondfunc(m,n):
    p = m - n
   # print(p)
    return p
# can't use local variable of one func in another function
c = 12
j = 10
k = 12
myfunc(j,k)

z = mysecondfunc(j,k)
print(z)

print(z + 90)'''
'''


#PROGRAM TO COUNT THE NO. OF DIGITS IN A  NUMBER

n = int(input('Enter any number: '))

print(len(str(n)))'''
'''

n = int(input('Enter the Number : '))


def LEN(n):
    count = 0
    #print(n)
    while n > 0:
     #   print(n)
        n = n // 10
        count += 1
    print(f'the number of digits is {count}')
    #print(n)
LEN(n)
#print(n)
'''
'''
n = int(input('Enter the Number : '))
x = 1
count = 0

while True:
    if n // x != 0:
        count += 1
        x = x * 10
    else:
        break

print(count)'''

def add():
    a = 12
    b = 34
    c = a + b
    return(c)
    print(a)

def sub():
    p = 4
    m = 3
    n = p-m
    return n



a  = sub()
print(a)
add()





