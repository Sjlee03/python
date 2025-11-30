nlist = [11, 4, 7, 15, 8, 9, 10, 3]

evenlist = []
oddlist = []

for num in nlist:
    if num % 2 == 0:
        evenlist.append(num)
    else:
        oddlist.append(num)
print(evenlist)
print(oddlist)
