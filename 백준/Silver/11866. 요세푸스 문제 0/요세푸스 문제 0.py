import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    queue = deque([i for i in range(1, N + 1)])

    rtn = []
    while queue:
        queue.rotate(-(K-1))
        rtn.append(str(queue.popleft()))

    print("<%s>" % (", ".join(rtn)))
