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
    print("%d %d"%(low, high))
    mid = (high+low)//2  # box number
    print("mid = %d"%(mid))
    dotori = 0
    # 도토리 개수 계산
    for i in range(k):
        # 현재 상자번호보다 해당 규칙의 스타팅 포인트가 크면 패스
        if mid < rules[i][0]:
            continue
        numD = 0
        if mid > rules[i][1]: # mid가 해당 규칙의 끝자리보다 큰 경우
            for j in range(rules[i][0],rules[i][1]+1,rules[i][2]):
                print("j = %d"%(j))
                numD += 1
        else: # mid가 해당 규칙의 끝자리보다 작거나같은 경우
            for j in range(rules[i][0],mid+1,rules[i][2]):
                print("j = %d"%(j))
                numD += 1
        dotori += numD
    print("dotori = %d\n--------------"%(dotori))

    if dotori >= d:
        res = mid
        high = mid-1
    else :
        low = mid+1

print(res)