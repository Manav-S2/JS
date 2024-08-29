#func = lambda arg: exp
#func(arg)


# MAP FUNC
'''
def square(n):
    return n * n

#n = int(input('Enter any value: '))

n = [1,2,3,4,5,6]

for i in n:
    b = square(i)
    print(b)


s = map(square,n)
print(list(s))
print(type(s))



def square(a):
    return a * a

l = (1,2,3,45,5,6,6,6,1,2,3,4,5,6,6)
b = {1:'one',2:'two',3:'three'}

#print(square.__doc__)
s = map(square,b)
print(tuple(s))
print(list(s))
for i in s:
    print(s)

#print(dict(s))

li = [1,2,3,4,5]

def square(x):
    return x ** 2

print(list(map(square,li)))

list1 = [1,2,3,4]

print(list(map(lambda x: x ** 2,list1 )))


def length(S):
    return len(S)

list1 = ['String', 'Wing', 'deutsh']

a = map(length,list1)
print(list(a))
print(tuple(a))
for i in a:
    print(i)
a = [12,23,43]
list1 = ['String', 'Wing', 'deutsch']
print(list(map(lambda x,y: len(x) * a, list1, a)))


def checkeven(n):
    if (n % 2 == 0):
        return n

ml = [1,2,3,4,5,6,7,8,9]
c = filter(checkeven, ml)

print(list(c))



def _Mo3(num):
   return num % 3 == 0
      #  return num

ml = [1,2,3,5,6,4,7,8,9]

c = filter(_Mo3, ml)
d = map(_Mo3, ml)
print(list(c))
print(list(d))

'''


ml = [1,2,3,4,5,6,7,8,9]

print(list(map(lambda x: x % 2 == 0, ml)))

print(list(filter(lambda x: x % 2 == 0, ml)))





