import sys

a,b = map(int, sys.stdin.readline().split(' '))
chessTile = []

for i in range(a) :
    chessTile.append(sys.stdin.readline().strip())
resList = []
for n in range(a-7) :
    for m in range(b-7) :
        fw = 0
        fb = 0
        for x in range(n, n + 8) :
            for y in range(m, m + 8) :
                if (x+y)%2 == 0 :
                    if chessTile[x][y] != "W" :
                        fw += 1
                    if chessTile[x][y] != "B" :
                        fb +=1
                else :
                    if chessTile[x][y] != "B" :
                        fw +=1
                    if chessTile[x][y] != "W" :
                        fb +=1
        resList.append(fw)
        resList.append(fb)

print(min(resList))