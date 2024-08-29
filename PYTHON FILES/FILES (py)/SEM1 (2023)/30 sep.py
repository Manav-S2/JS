# str of length 1 is called a character
'''
s = 'welcome'
print(s[3])
print(s[-3])
print(s[2:13])

l = ['hello']
print(l[0][0])'''

'''
matrix = [[1,2,3,4], [5,6,7,8],[9,10,11,12]]
transpose = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matrix)):
    for j in range(len(transpose)):
        transpose[j][i] = matrix[i][j]
print(matrix)
print(transpose)

a = int(input('n: '))
temp = a
s = 0

c = 0
while a > 0:
    a //= 10
    c += 1

print(c)

for i in range(c):
    d = temp % 10
    print(d)
    temp //= 10
    s += d ** c

print(s)

num = int(input('Enter any number: '))

length = len(str(num))

temp = num

s = 0

while temp > 0:
    digit = temp % 10
    s += digit ** length
    temp //= 10

print(s)

if num == s:
    print('armstrong number')
else:
    print('not an armstrong number')

num = int(input('n: '))
length = len(str(num))
temp = num
s = 0

while temp > 0:
    digit = temp % 10
    s += (digit ** length)
    temp //= 10

print(s)
'''
'''
column = int(input('c : '))
rows = int(input('r : '))
parts = []
m = []

for i in range(rows):
    for i in range(column):
        a = int(input('enter columns: '))
        parts.append(a)
    m.append(parts)
    parts = []
print(m)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
rows = len(m)
columns = len(m[0])

transpose = []
part = []
for i in range(columns):
    transpose.append(part)
    for j in range(rows):
        part.append(0)
    part = []
print(transpose)

for i in range(rows):
    for j in range(columns):
        transpose[j][i] = m[i][j]
print(transpose)



'''
'''

x = int(input('enter x: '))

y = 100 if x > 10 else 200
print(y)

a,b = 7,6
c = a if a % 2 == 0 else b
print(a,b,c)'''



