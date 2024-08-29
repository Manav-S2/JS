# a = ([12,23],[233,345])
# print(dict(a))
# b = 3
# a = {'a' : 1, b : 2, 'c': 3}
# b = 4
# print(a['a'])
# print(a.get('b'))
#
# l = [1,2,3,4,55,]
# print(a.values())
# print(a.get(b))
#
# a = {'a': 1, 'b': 2, 'c': 3}
# a['b'] = 4
# print(a)
# a['d'] = 5
# print(a)
#
#
# #
# a = (1,2,3,4,5)
#
# b = {3:2,34:2,45:3,45:23}
# c = {11,2,2,11,23,22}
# d = [11,2,2,11,23,22]
# print(list(zip(b)))
#
# print(list(zip(c)))
# print(list(zip(d)))
#
# d1 = input('enter data: ')
# d2 = input('enter data: ')
#
# l1 = d1.split(',')
# l2 = d2.split(',')
#
# if len(l1) != len(l2):
#     print('lists are of different lengths')
# else:
#     print(list(zip(l1, l2)))
# #
# a =  [1,23,4]
# b = [2,33,43]
# print()
# print(sorted(dict(zip(a,b))))
# print(sorted(dict(zip(a,b)).items()))
#
# a = {1:2,2:3,3:4}
# print(sorted(a.items()))
#
# # for k,v in (a.items()):
# #     print(k,v)
# #
#
# # a = [1,23,4]
# # b = [6,4,5]
# print(sorted(a))
#
# dictone = {1 : 'C', 2 : 'C#' , 3 : 'SQL'}
# dictone.pop(1)
# print(dictone)
#
# dictone.popitem()
# print(dictone)
#
# #del dictone[2]
# dictone.clear()
# del dictone
# #print(dictone)
#
#
# d = {1:2,3:4,5:5}

#
# a = [1,2,3,4]
# b = ['w', 'e','d']
# print(sorted(dict(zip(a,b))))
#
#
# a = {2 :'',(8,0) : 2}
#
# # print(all(a))
#
# # a = {1,23,4}
# # b= {1,23,4}
# # print(a is b)
#
# b = a.copy()
# print(b)
# dictone = {}
# tupleone = ('python' , 'java' ,' c')
# b = [1,2,3]
#
# dictone = dictone.fromkeys(tupleone, b)
# print(dictone)
# x = set([1, 2, 3])
# y = x
#
# y |= set([4, 5, 6])
# print(y)
# print(x)
# print(x is y)

dicto = {1:2, 2: 3, 4:6}
print(dicto.setdefault(5, 9))