# 22/07/21
import sys

n,c = map(int,sys.stdin.readline().strip().split())
houseX = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])
distance_bet = []

for x in range(n) :
    if x == 0: continue
    distance_bet.append(houseX[x]-houseX[x-1])

low = 0
high = houseX[-1] - houseX[0]
ans = 0
a=0
while low<=high:
    mid = (high+low)//2
    distance_list = []
    cnt = 1
    total_distance = 0

    for i in range(n-1):
        if total_distance+distance_bet[i] >= mid:
            distance_list.append(total_distance)
            cnt += 1
            total_distance = distance_bet[i]
        else :
            total_distance += distance_bet[i]

    if total_distance:
        distance_list.append(total_distance)
        cnt += 1

    res = min(distance_list)
    if cnt >= c:
        a = mid
        ans = max(res,ans)
        low = mid+1
    else :
        high = mid-1

print(ans)
