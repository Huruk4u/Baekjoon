# 22/07/20
import sys

n,m = map(int,sys.stdin.readline().strip().split())
expense = [int(sys.stdin.readline().strip()) for _ in range(n)]

low = max(expense)
high = sum(expense)


def finder(mid):
    total = mid
    cnt = 0
    for i in range(n):
        if total-expense[i] < 0 :
            cnt += 1
            total = mid
        total -= expense[i]
    if total != mid :
        cnt += 1
    return cnt


while low <= high:
    mid = (high+low)//2
    res = finder(mid)

    if res > m :
        low = mid+1
    else :
        ans = mid
        high = mid-1

print(ans)