# 22/08/26
import sys
from collections import deque as dq

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n,loc = map(int,sys.stdin.readline().strip().split())
    priority = dq(map(int,sys.stdin.readline().strip().split()))
    target = dq([0]*n)
    target[loc] = 1
    cnt = 0
    while True :
        if priority[0] == max(priority):
            if target[0] == 1:
                target.popleft()
                cnt += 1
                break
            priority.popleft()
            target.popleft()
            cnt += 1
        else:
            priority.append(priority.popleft())
            target.append(target.popleft())
    print(cnt)
