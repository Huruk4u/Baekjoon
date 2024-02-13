# 22/08/03
import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

low = 0; high = k
res = 0
while low<=high:
    mid = (low+high)//2
    cnt = 0

    for x in range(1,n+1):
        cnt += min(mid//x,n)

    if cnt < k:
        low = mid+1
    else:
        res = mid
        high = mid-1

print(res)