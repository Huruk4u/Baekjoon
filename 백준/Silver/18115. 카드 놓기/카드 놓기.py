import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    command = list(map(int, input().strip().split()))
    command.reverse()

    card = deque()
    for i in range(N):
        if command[i] == 1:
            card.appendleft(i+1)
        elif command[i] == 2:
            card.insert(1, i+1)
        else:
            card.append(i+1)

    print(*card)

