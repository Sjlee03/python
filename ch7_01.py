nlist = [3, 5, 1, 6, 8 ,7]

cnt = nlist.count(3)
print(cnt)

for i in range(1, 10):
    print(i, nlist.count(i))
print('\n')

for i in range(1, 10):
    if nlist.count(i) == 0:
        nlist.append(i)
nlist.sort()
print(nlist)
