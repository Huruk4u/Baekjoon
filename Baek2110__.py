# 22/07/21
import sys

n,c = map(int,sys.stdin.readline().strip().split())
houseX = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])

low = 0
high = houseX[-1]-houseX[0]
ans = 0

while low<=high:
    mid = (high+low)//2
    totalX = houseX[0]
    cnt = 1

    for i in range(n):
        if houseX[i] >= totalX+mid:
            cnt += 1
            totalX = houseX[i]

    if cnt >= c:
        ans = mid
        low = mid+1
    else:
        high = mid-1

print(ans)