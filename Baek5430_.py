# 22/08/27
import sys
from collections import deque

input = sys.stdin.readline
T = int(input().strip())

for _ in range(T):
    command = deque(input().strip())
    p = int(input().strip())
    arr = deque(input().rstrip()[1:-1].split(","))
    if p == 0: arr = deque()
    direction = 1
    error = False
    for c in command:
        if c == "R":
            direction *= -1
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
        print('error')
        continue
    else:
        if direction == 1:
            print('['+','.join(arr)+']')
        else :
            print('['+','.join(reversed(arr))+']')