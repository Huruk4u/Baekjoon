import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    queue = deque([i + 1 for i in range(N)])

    step = 1
    for i in range(1, N):
        rotate_cnt = ((step ** 3) % len(queue)) - 1
        if rotate_cnt == -1:
            queue.rotate()
        else:
            for _ in range(rotate_cnt):
                queue.rotate(-1)
        queue.popleft()
        step += 1

    print(queue[0])
