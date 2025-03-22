import sys
from pprint import pprint
input = sys.stdin.readline
INF = sys.maxsize


if __name__ == '__main__':
    N = int(input().strip())
    dist = [[INF] * (N+1) for _ in range(N+1)]
    while True:
        u, v = map(int, input().strip().split())
        if u == -1 and v == -1:
            break
        dist[u][v] = 1
        dist[v][u] = 1

    for i in range(1, N+1):
        dist[i][i] = 0

    for k in range(1, N+1):
        for u in range(1, N+1):
            for v in range(1, N+1):
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

    score = [0] * (N+1)
    for i in range(1, N+1):
        score[i] = max(dist[i][1:N+1])

    min_score = min(score[1:N+1])
    answer = []
    for i in range(1, N+1):
        if score[i] != min_score: continue
        answer.append(i)

    print(min_score, len(answer))
    print(*answer)
