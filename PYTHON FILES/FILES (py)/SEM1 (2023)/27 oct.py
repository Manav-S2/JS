#
# # a3 = [1,2,34,'vdv',-34, '']
# # print(all(a3))
# #
# #
# # l2 = [1,2,3,4,'23', '', 0]
# # l3 = []
# # print(any(l3))
#
# a = ['python', 'java', 'c', 'c++','r']
#
# print(list(enumerate(a)))
# print(enumerate(a))
#
# l = len(a)
# print(l)
#
# mq = max(a)
# print(mq)
#
#
# b = [1,2,44,32,11,34]
# print(max(b))
#
# print(sorted(b,reverse = True))
#
# s = 'def'
# print(s.count('d'))
# print(b.count(1))
#
# print(sum(b))


#
#
# #tuple
#
# tupleone = (1,4,8,12,16)
# print(tupleone[::])
#
# print(tupleone[1:4])
#
# print(tupleone[::-1])
# print(sorted(tupleone,reverse = True))
# tupletwo = (2,34,5,3.4)
# print(max(tupletwo))
#
# print(tupleone + tupletwo)
#
# # a = tuple()
# # print(a)
# #
# # print(type(a))
# print(tupleone * 2)
#
#
# #
# # b = (1,)
# # print(type(b))
# #
# # a = {}
# # print(type(a))
#
# print(tupleone)
# print(4 in tupleone)
#
# print(2 not in tupleone)
# print(tupleone == tupletwo)
#
#
# a = (1,2,3,4)
# b = (1,2,3)
#
# print(a >= b)
#
# print(any(a))
# print(all(a))
#
# print(set(enumerate(a)))
#
# for i in enumerate(a):
#     print(i)
#
#
# print(sorted(a,reverse = True))
#
# tup = ()
# a = list(tup)
#
# n = 'n'
# i = 0
#
# while n == 'n':
#     element = input("Enter value: ")
#     a.append(element)
#     n = input('Press n, if not done done: ')
#     i += 1
# tup = tuple(a)
# print(tup)
# print('len of string =', i)
#
#
# d = input('data: ')
# #a = tuple(d.split(','))
# a = tuple(d.split())
#
# print(len(a))



'''dictionaries'''


# print(dict(enumerate(t)))
#
# t = {1,3432,'dwd',32, 23,4,5}



#
#
#
#
#
# dic = {1:23,'323':323,'dw': 323}
# dic[1] = 332
# print(dic[1])
#
# a  = dict()
#
#
# a = {1,2,3,4}
# b = list(enumerate(a))
# print(b)
# print(dict(b))
#
#
#
# a = [([(1)])]
# print(a)
# print(type(a))

#
# d = {'rep':1, 'bep': 2, 'sep': 3}
# d['dep'] = 4
# print(d)
# print(d.get('sep'))
#
# d['sep'] = 'w'
# print(d)
#
#
# print(d.get('dep'))
# print(d.pop('sep'))
# print(d)
#
# d.clear()
# print(d)




l1 = [1,2,3]
l2 = ['python','java','c++','c%']
l3 = ['a','b','c']
print(list(zip(l1,l2,l3)))
#print(dict(zip(l1,l2,l3)))





