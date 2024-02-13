# 22/08/13
import sys
from collections import deque

num = 2
sys.stdin = open('C:/Users/sungm/Desktop/test_data/editor.in' + str(num), 'r')
print(open('C:/Users/sungm/Desktop/test_data/editor.ou' + str(num), 'r').readline())

left = deque(sys.stdin.readline().strip())
right = deque([])
m = int(sys.stdin.readline().strip())

for i in range(m):
    command = list(sys.stdin.readline().split())
    print("====================\n command is ",command)
    if command[0] == 'P':
        left.append(command[1])
    elif command[0] == 'L' and left:
        right.appendleft(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.popleft())
    elif command[0] == 'B' and left:
        left.pop()
    print(left,right)

print(''.join(left + right))