import sys

listA = []
listB = []
for i in range(3) :
    x,y = map(int,sys.stdin.readline().split(' '))
    listA.append(x)
    listB.append(y)
n = 0
m = 0
for a in listA :
    if listA.count(a)%2 != 0 :
        n = a

for b in listB :
    if listB.count(b)%2 != 0 :
        m = b

print(f"{n} {m}")