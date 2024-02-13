# 22/07/15
import sys

n = int(sys.stdin.readline().strip())
budget = list(map(int,sys.stdin.readline().strip().split()))
possibleB = int(sys.stdin.readline().strip())

def finder(low,high) :
    mid = (low+high)//2
    print("range %d -- %d ------"%(low,high))
    print("mid = %d"%(mid))
    totalB = 0
    if (high-low) <= 1:
        print(low)
        return
# 요청이 예산보다 많으면 배정된 예산으로. else 요청대로
    for i in range(n):
        print("Call = %d"%(budget[i]))
        if budget[i] > mid:
            totalB += mid
            print("total + mid =%d"%(totalB))
        else :
            totalB += budget[i]
            print("total + call =%d"%(totalB))
# 총 예산이 가능한 예산보다 많으면, 더 작은 구간에서 탐색
    if totalB > possibleB:
        finder(low,mid)
    else :
        finder(mid,high)

finder(0,max(budget)+1)