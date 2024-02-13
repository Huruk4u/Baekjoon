# 22/08/25
import sys

n,p = map(int,sys.stdin.readline().strip().split())
melody = []
for _ in range(n):
    l, f = map(int, sys.stdin.readline().strip().split())
    melody.append([l, f])

guitar = []
for _ in range(6):
    guitar.append([0])

stack = []; cnt = 0
for line, fret in melody:
    if fret > guitar[line-1][-1]:
        guitar[line-1].append(fret)
        cnt += 1
    else:
        if guitar[line-1]:
            while guitar[line-1][-1] > fret:
                guitar[line-1].pop()
                cnt += 1
        if guitar[line-1][-1] == fret:
            continue
        else:
            guitar[line-1].append(fret)
            cnt += 1

print(cnt)