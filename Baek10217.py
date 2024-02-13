import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N, M, K = map(int, input().split())
        graph = [[] for _ in range(N + 1)]

        for _ in range(K):
            u, v, c, d = map(int, input().split())
            graph[u].append((v, c, d))

        dist = [[INF] * (M+1) for _ in range(N+1)]
        dist[1][0] = 0

        for cost in range(M+1):
            for n in range(1, N + 1):
                if dist[n][cost] == INF:
                    continue
                time = dist[n][cost]
                for next, c, t in graph[n]:
                    if c + cost > M:
                        continue
                    dist[next][c + cost] = min(dist[next][c + cost], time + t)

        ans = min(dist[N])

        print(ans if ans != INF else "Poor KCM")
