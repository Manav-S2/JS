# num1 = int(input('Enter Num 1: '))
# num2 = int(input('Enter Num 2: '))
# num3 = int(input('Enter Num 3: '))
#
# def maximum(a,b,c):
#     return max(a,b,c)
#     print('Hello')
#
# print(f'largest of the value entered is: {maximum(num1,num2,num3)}')
# maximum(num1,num2,num3)
import math

x = int(input('Enter X: '))
y = int(input('Enter Y: '))

def computeGCD(x,y):
    return math.gcd(x,y)

print(computeGCD(x,y))
