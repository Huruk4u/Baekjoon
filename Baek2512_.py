# 22/07/15
import sys

n = int(sys.stdin.readline().strip())
budget = list(map(int,sys.stdin.readline().strip().split()))
possibleB = int(sys.stdin.readline().strip())

def finder(low,high) :
    mid = (low+high)//2
    totalB = 0
    if (high-low) <= 1:
        print(low)
        return

    for i in range(n):
        if budget[i] > mid:
            totalB += mid
        else :
            totalB += budget[i]

    if totalB > possibleB:
        finder(low,mid)
    else :
        finder(mid,high)

finder(0,max(budget)+1)