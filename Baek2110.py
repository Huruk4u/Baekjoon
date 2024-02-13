# 22/07/21
import sys

n,c = map(int,sys.stdin.readline().strip().split())
houseX = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])
distance_bet = []

for x in range(n) :
    if x == 0: continue
    distance_bet.append(houseX[x]-houseX[x-1])

low = 0
high = sum(distance_bet)
ans = 0

while low<=high:
    print("%d %d"%(low, high))

    mid = (high+low)//2
    print("mid = %d-----------"%(mid))

    distance_list = []
    cnt = 1
    total_distance = 0

    for i in range(n-1):
        print("distance = %d"%(distance_bet[i]))
        if total_distance+distance_bet[i] >= mid:
            print("reset")
            distance_list.append(total_distance)
            cnt += 1
            total_distance = distance_bet[i]
        else :
            total_distance += distance_bet[i]

    if total_distance :
        distance_list.append(total_distance)
        cnt += 1

    res = min(distance_list)
    print(distance_list)
    print("res = %d"%(res))
    print("cnt = %d\n---------------"%(cnt))
    if cnt >= c: #조건충족
        ans = max(res,ans)
        low = mid+1
    else :
        high = mid - 1
print(ans)