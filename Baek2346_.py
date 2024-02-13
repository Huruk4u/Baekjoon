# 22/08/11
import sys,collections

n = int(sys.stdin.readline().strip())
a = list(map(int,sys.stdin.readline().strip().split()))
arr = collections.deque(a)
temp = 0; jump = 0

while arr:
    # pick
    if temp == 0:
        print(a.index(arr[0])+1,end=' ')
        jump = arr[0]
        arr.popleft()

    if jump > 0:
        arr.rotate((jump-1)*(-1))
    else :
        arr.rotate(jump*(-1))