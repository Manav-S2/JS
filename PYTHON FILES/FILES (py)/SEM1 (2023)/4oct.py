'''1for i in range(5):
    if i == 3:
        break
    print(i)


else:
    print('i else')

a  = 6
while a > 0:
    print(a)
    a -= 1
    if a == 2:
        break

else:
    print('Done')


#function - set of statements that perform some task.

def boy(name, age):                     #2
    print(name,'is',age,'years old')    #3

boy('john', 22)               #1
boy(age = 22, name = 'john')





def boy(* args):
    print(args)
    for i in range(len(args)):
        print(args[i])

    print(f'{args[0]} is {args[1]} year old and is roll no {args[2]}')
    # arg = [name,age, rollno adm no]
    #for i in range(len(args)):
     #   print(f'{i[0]} is {i[1]} year old and is roll no {i[2]}')

boy('12','312')
boy (12,34,45)boy('john',23, 21)




def mysum(* args):
    totalsum = 0
    for i in args:
        totalsum += i
    print(totalsum)


mysum(1232,45,45)
'''








def a(a,b):
    print(a-b)
a(4,4)
a(b =1, a =2)
a(a = 2, b = 4)
a(3,b=4)
#a(a = 4, 5)
a(2,a =4)











