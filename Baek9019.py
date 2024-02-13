import sys
from collections import deque

input = sys.stdin.readline


def bfs(queue):
    while queue:
        cn, opr = queue.popleft()
        if cn == B:
            return opr

        # D
        nn = (cn * 2) % 10000
        if not visited[nn]:
            queue.append((nn, opr + 'D'))
            visited[nn] = 1

        # S
        nn = (cn - 1) % 10000
        if not visited[nn]:
            queue.append((nn, opr + 'S'))
            visited[nn] = 1

        # L
        nn = (cn % 1000) * 10 + cn // 1000
        if not visited[nn]:
            queue.append((nn, opr + 'L'))
            visited[nn] = 1

        # R
        nn = (cn % 10) * 1000 + cn // 10
        if not visited[nn]:
            queue.append((nn, opr + 'R'))
            visited[nn] = 1


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        A, B = map(int, input().strip().split())

        visited = [False for _ in range(10001)]
        visited[A] = True
        queue = deque()
        queue.append((A, ''))

        print(bfs(queue))
