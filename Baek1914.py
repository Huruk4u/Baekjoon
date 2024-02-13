import sys

n = int(sys.stdin.readline().strip())

def hanoi(n, start, mid, end) :
    if n == 1 :
        print(start, end)
    else:
        hanoi(n-1,start,end,mid) #1
        hanoi(1,start,mid,end) #2
        hanoi(n-1,mid,start,end) #3

if n > 20 :
    print((2**n)-1)
else :
    print((2**n)-1)
    hanoi(n,1,2,3)