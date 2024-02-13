# 22/08/19
import sys
from collections import deque as dq

n = int(sys.stdin.readline().strip())
res = []
for _ in range(n):
    command = list(sys.stdin.readline().strip())
    front = dq()
    end = dq()
    for i in range(len(command)):
        if command[i] == '<':
            if bool(front) == False :
                continue
            end.appendleft(front.pop())
        elif command[i] == '>':
            if bool(end) == False :
                continue
            front.append(end.popleft())
        elif command[i] == '-':
            if bool(front) == False:
                continue
            front.pop()
        else:
            front.append(command[i])

    print(''.join(front+end))