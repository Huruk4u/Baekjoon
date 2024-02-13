import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize


def bf(start):
    time = [INF] * (N+1)
    time[start] = 0
    for i in range(N):
        for u, v, dt in edge:
            new_time = time[u] + dt
            if new_time < time[v]:
                time[v] = new_time
                if i == N-1:
                    return True
    return False


if __name__ == '__main__':
    TC = int(input().strip())
    for _ in range(TC):
        N, M, W = map(int, input().strip().split())

        edge = []
        for _ in range(M):
            s, e, t = map(int, input().strip().split())
            edge.append([s, e, t])
            edge.append([e, s, t])
        for _ in range(W):
            s, e, t = map(int, input().strip().split())
            edge.append([s, e, -t])

        minusCycle = bf(1)

        if minusCycle:
            print("YES")
        else:
            print("NO")
