import sys

l,w,h = map(int,sys.stdin.readline().strip().split())

n = int(sys.stdin.readline().strip())
cubes = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
cubes.sort(reverse=True)
res = before = 0

for lv, nc in cubes :
    before *= 8
    lenC = 2**lv
    cnt = (l//lenC) * (w//lenC) * (h//lenC) - before
    cnt = min(cnt,nc)

    res += cnt
    before += cnt

if before == (l*w*h) :
    print(res)
else : print(-1)