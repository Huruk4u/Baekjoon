import sys

n = int(sys.stdin.readline().strip())

yx = []

for _ in range(n):
    x,y = list(map(int,sys.stdin.readline().split(' ')))
    yxp = [y,x]
    yx.append(yxp)

sp = sorted(yx)
for i in range(n) :
    print(sp[i][1],sp[i][0])