##mylist = [1,2,3,4.5, 'hello', 'bye']
##print(mylist)
##print(mylist[2:5])
##print(mylist[2])
##print(mylist[-4])
##print(mylist[1:5])'''
'''
mylist = [1,4,3.5, 'Hello', 'bye', 6 ,7, 8]
print(mylist[-2])
print(mylist[3:0:-1])

print(mylist[1:6:2])'''


'''
mylist = [1,3.5,'Hello' , 7,8]

for i in mylist:
    print(i)'''

l = [1,2,3,4,5,6]

#2 components of  a function
def multiplylist(l):
    s = 1
    for i in l:
        s *= i
    print(s)

multiplylist(l )

