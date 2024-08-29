# l = [ i for i in range(1,11) if i % 2 == 0]
# print(l)

# s = {i for i in 'codetantra' if i not in 'tan'}
# print(s)
#
# a = [(1,2),(2,4)]
# d = {i:j for (i,j) in a  }
# print(d)

#
#
#
# l = [100,200,300]
# print(type(enumerate(l)))
# d = {i:j for (i,j) in enumerate(l)}
# print(d)
#
#
# d = {i :i**2 for i in range(0,10)}
# print(d)
# d = {1:2, 2:  3}
# print(d)
#
#
#
# d = {i:j for (i,j) in [(2,5)] }
# print(d)
#
# d = {k: 'python' for k in 'codetatra'}
# print(d)
#
#
# print({'a':2,'a':4})
m = 2
n = 3
mat = [[int(input()) for x in range (n)] for y in range(m)]

for i in range(m):
    for j in range(n):
        print(mat[i][j], end = ' ')
    print()


print(mat)
nz = []
r = []
c = []
for i in range(len(mat)):
    for j in  range(len(mat[0])):
        if mat[i][j] != 0:
            nz.append(mat[i][j])
            r.append(i)
            clovgcgd4fdfd.append(j)

print(r)
print(c)
print(nz)


