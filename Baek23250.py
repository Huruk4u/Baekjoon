import sys

n,k = map(int,sys.stdin.readline().strip().split())

def hanoi(n,k,start,mid,end) :
    mp = (((2 ** n) - 1) // 2) + 1
    if n == 1:
        print(start, end)
        return
    else :
        if k < mp :
            hanoi(n-1,k,start,end,mid)
        elif k == mp :
            hanoi(1,k,start,mid,end)
        else :
            hanoi(n-1,k-mp,mid,start,end)

hanoi(n,k,1,2,3)