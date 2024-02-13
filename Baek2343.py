# 22/07/20
import sys

n,m = map(int,sys.stdin.readline().strip().split())
lecture = list(map(int,sys.stdin.readline().strip().split()))

high = sum(lecture)
low = max(lecture)
ans = 1000000000000

def finder(mid):
    total_time = 0
    blueray_cnt = 0
    for i in range(n):
        if total_time + lecture[i] > mid:
            blueray_cnt += 1
            total_time = lecture[i]
        else :
            total_time += lecture[i]
    if total_time:
        blueray_cnt += 1
    return blueray_cnt

while high >= low:
    mid = (high+low)//2
    res = finder(mid)

    if res > m :
        low = mid+1
    else :
        ans = min(ans,mid)
        high = mid-1
print(ans)