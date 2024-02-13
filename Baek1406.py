# 22/08/13
import sys
from collections import deque

left = deque(sys.stdin.readline().strip())
right = deque()
m = int(sys.stdin.readline().strip())

for i in range(m):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'P':
        left.append(command[1])
    elif command[0] == 'L' and left:
        right.appendleft(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.popleft())
    elif command[0] == 'B' and left:
        left.pop()

print(''.join(left+right))