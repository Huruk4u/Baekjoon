# 22/07/28
import sys

n,k,d = map(int,sys.stdin.readline().strip().split())
rules = []

for _ in range(k):
    r = list(map(int,sys.stdin.readline().strip().split()))
    rules.append(r)

low = 0
high = n
res = 0

while low<=high:
    mid = (high+low)//2  # box number
    dotori = 0

    # 도토리 개수 계산
    for i in range(k):
        if mid < rules[i][0]:
            continue
        start = rules[i][0]; end = rules[i][1]; jump = rules[i][2]
        e = min(end,mid)
        numD = (e-start)//jump + 1

        dotori += numD

    if dotori >= d:
        res = mid
        high = mid-1
    else :
        low = mid+1

print(res)