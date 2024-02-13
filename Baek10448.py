import sys

res = [0] * 1001
tri = [n*(n+1)//2 for n in range(1,46)]

for x in tri:
    for y in tri:
        for z in tri:
            if x+y+z <= 1000:
                res[x+y+z] = 1

T = int(sys.stdin.readline().strip())

ans = []
for _ in range(T) :
    n = int(sys.stdin.readline().strip())
    print(res[n])