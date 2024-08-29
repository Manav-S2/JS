l1 = input('data1: ').split(',')
l2 = input('data2: ').split(',')

d = dict(zip(l1,l2))

a = []
b = []
for i in d.keys():
    a.append(i)

for i in d.values():
    b.append(i)

print(a)
print(b)

for 