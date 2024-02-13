# 22/07/19
import sys

n,m = map(int,sys.stdin.readline().strip().split())
lecture = list(map(int, sys.stdin.readline().strip().split()))

a = max(lecture)
b = sum(lecture)+1

def finder(low,high):
    mid = (low+high)//2
    if (high-low) <= 1:
        print(low)
        return

    totalT = 0
    numBlue = 0

    for i in range(n):
        if (totalT + lecture[i]) > mid:
            numBlue += 1
            totalT = lecture[i]
        else :
            totalT += lecture[i]

    if numBlue :
        numBlue += 1
    if numBlue > m:
        finder(mid,high)
    else :
        finder(low,mid)

finder(a,b)