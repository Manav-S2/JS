# if we intend to multiply a number n times
#then rather than multiplying it sttraight away with not
#
#a * b = a + +a+a+a+a+a+++ b times
# a * b = a + a*(b-1)= a + a + a(b-2)+ a + a+ a + a*(b-3)+__________

# b = int(input('enter b: '))
# a = int(input('enter a: '))
# def mult(a,b):
#     if b == 1:          #base case
#         return a
#     else:
#         return a + mult(a,b-1)
#
#
# ans = mult(a,b)
# print(ans)

n = int(input('Enter Number: '))

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

a = fac(n)
print(a)