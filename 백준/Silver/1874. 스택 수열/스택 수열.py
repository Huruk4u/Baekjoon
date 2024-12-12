import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    copy_perm = deque([int(input().strip()) for _ in range(N)])

    stack, command = [], []
    for i in range(1, N+1):
        # push
        stack.append(i)
        command.append("+")
        while stack and copy_perm and stack[-1] == copy_perm[0]:
            copy_perm.popleft()
            # pop
            stack.pop()
            command.append("-")

    if len(command) != N*2:
        print("NO")
    else:
        for i in range(N*2):
            print(command[i])
