num = [i for i in range(1,10001)]
numset = set(num)

notSelf = set()

for number in numset :
    a = 0
    selfnum = 0
    for i in list(str(number)) :
        a += int(i)
    selfnum += a + number
    notSelf.add(selfnum)

numList = list(numset - notSelf)
numList.sort()
for j in numList :
    print(j)