import sys

N,M,B = map(int,sys.stdin.readline().split(' '))
field = [list(map(int,sys.stdin.readline().split())) for u in range(N)]

h = 0
res = 111111111111111110
for i in range(257):
    work1 = 0
    work2 = 0
    for n in range(N) :
        for m in range(M):
            if field[n][m] < i:
                work2 += (i - field[n][m])
            elif field[n][m] > i:
                work1 += (field[n][m] - i)
    blocks = work1 + B

    if blocks < work2 :
        continue
    time = (2*work1) + work2
    if time <= res :
        res = time
        h = i

print(res, h)