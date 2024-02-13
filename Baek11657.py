import sys
input = sys.stdin.readline
INF = sys.maxsize


def bf(start):
    time[start] = 0
    for i in range(1, N+1):
        for u, v, weight in edge:
            # 현재 노드의 최솟값이 갱신되지 않았다면, 이후 과정은 의미가 없음.
            if time[u] == INF:
                continue
            if time[u] + weight < time[v]:
                time[v] = time[u] + weight
                if i == N:
                    return True
    return False


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    edge = []
    for _ in range(M):
        a, b, c = map(int, input().strip().split())
        edge.append([a, b, c])

    time = [INF] * (N + 1)
    minusCycle = bf(1)

    if minusCycle:
        print(-1)
    else:
        for i in range(2, N+1):
            if time[i] == INF:
                print(-1)
            else:
                print(time[i])
