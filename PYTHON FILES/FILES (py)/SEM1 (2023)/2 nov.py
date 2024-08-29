# dictone = {1  :'Python', 2 : 'Java', 3 : 'C'}
# print(dictone.setdefault(4, 'c'))
# print(dictone)
#
#
# dicttwo = {4: 'Javascript', 5 : 'R'}
#
# dictone.update(dicttwo)
#
# print(dictone)
# # print(dicttwo)
# #
# # a = [1,2,3,4]
# # d = {}
# # print(d.fromkeys(a,2))
#
# a = {1,23,3,4,5, (32,34,4), '23', True, False}
# print(a)
# print(len(a))
# b = a.copy()
# print(b)
# # print(1 in a)
# print(id(a) , id(b))
# print(a is b)
# \\
# a = {1,23,3,4,5, (32,34,4), '23', True, False}
# b = {1,23,4,5}
# c = {1,23,4,5}
#
# print(a.isdisjoint(b))
# print(b.issubset(a))
# print(b.issubset(c))
# print(c.issubset(b))
# print(a.issuperset(b))
# c = b
# print(c is b)




l = [i for i in range(1,11) if i % 2 == 0]
print(l)

a = input('str: ')
l = [i for i in a]
print(l)