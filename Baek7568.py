import sys

n = int(sys.stdin.readline().strip())

Hlist = []

for _ in range(n):
    wage, tall = map(int,sys.stdin.readline().split(' '))
    listH = (wage,tall)
    Hlist.append(listH)

res = []

for i in range(len(Hlist)):
    rank = len(Hlist) + 1
    for j in range(len(Hlist)):
        if Hlist[i][0] >= Hlist[j][0] and Hlist[i][1] >= Hlist[j][1]:
            rank -= 1
        elif Hlist[i][0] >= Hlist[j][0] or Hlist[i][1] >= Hlist[j][1]:
            rank -= 1
        else : pass
    res.append(str(rank))

resS = " ".join(res)
print(resS)