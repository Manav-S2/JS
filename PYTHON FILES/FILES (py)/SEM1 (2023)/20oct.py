# #fib
# n = 10
#
# f1 = 0
# f2 = 1
# sum = 0
#
# print(f1)
# for i in range(n):
#     f1 = f2
#     f2 = sum
#     sum = f1 + f2
#     print(f2)
#     print(sum)
#     if (f2>n):
#         break
#
#
#
#
# def fib(n):
#     # if n <= 1:
#     #     return n
#     # else:
#         return fib(n-1)+fib(n-2)
#
# n = int(input('Enter the  number of terms: '))
# for i in range(n):
#     print(fib(i))
#
# print(fib(-5))
#
# def square(x):
#     return x ** 2
#
# def double(x):
#     return(x * 2)
#
# n = int(input('Enter any number: '))
#
# print(square(double(n)))
#

# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# n = int(input('Enter any number: '))
# print(fib(n))



# a = 20
# print(dir(b))
# b = [4]
# #print(dir(a))
# print(b.__contains__(3))
#
#


# a = 'sdnk.ekn ece,ce'
# print(a[4]+a[8]+a[12]+a[-3])
#
# print(a[:3:-1])
#
#
#



# for i  in range(-123):
#     print(i)



# a = 'what did u say?'
# c = len(a)
# print(type(c))
# b = a[1:c]
# print(b)

f1 = 0
f2 = 1
sum = 0
n = 5
i =0

print(f1)
while i <= n:
    f1 = f2
    f2 =  sum
    sum = f1 + f2
    if i < n:
        print(sum)
    else:
        break
    i += 1



