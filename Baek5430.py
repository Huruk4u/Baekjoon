# 22/08/27
import sys
from collections import deque

input = sys.stdin.readline
T = int(input().strip())

for _ in range(T):
    command = deque(input().strip())
    p = int(input().strip())
    arr = deque(input().strip()[1:-1].split(","))
    direction = 1
    error = False
    for c in command:
        print("===============\ncommand is %s" % (c))
        print("arr is ",arr)
        if c == "R":
            direction *= -1
            print("direction is %d"%(direction))
        elif c == "D":
            if not arr :
                error = True
                break
            else:
                if direction == 1:
                    arr.popleft()
                else:
                    arr.pop()
    if error:
        print("error")
    else :
        if direction == 1:
            print('['+','.join(arr)+']')
        else :
            print('['+','.join(reversed(arr))+']')