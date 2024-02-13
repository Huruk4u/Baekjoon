# 22/08/26
import sys
from collections import deque as dq

n = int(sys.stdin.readline().strip())
q = dq()

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        if not q:
            print(-1)
        else :
            print(q.popleft())
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if q:
            print(q[0])
        else :
            print(-1)
    elif command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)