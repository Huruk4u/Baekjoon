import sys

n = int(sys.stdin.readline().strip())
pp = []


for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    p = [x,y]
    pp.append(p)

ppp = sorted(pp)

for i in range(n):
    print(ppp[i][0], ppp[i][1])