import sys
from collections import deque
input = sys.stdin.readline


def start_node():
    q = deque([])
    for i in range(1, N+1):
        if not inDeg[i]:
            q.append(i)
            inDeg[i] = -1

    return q


def tsort():
    queue = start_node()
    while queue:
        curr = queue.popleft()
        rtn.append(curr)
        for i in range(1, N+1):
            if not graph[curr][i]:
                continue
            inDeg[i] -= 1

        cnt = 0
        for i in range(1, N+1):
            if not inDeg[i]:
                queue.append(i)
                inDeg[i] = -1
                cnt += 1

        if cnt > 1:
            return False

    return True


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())

        lastRank = list(map(int, input().strip().split()))
        graph = [[False] * (N+1) for _ in range(N+1)]   # 간선 방향 빠르게 바꿀려고 matrix로 만듬
        inDeg = [0 for _ in range(N+1)]
        for i in range(N):
            for j in range(i+1, N):
                graph[lastRank[i]][lastRank[j]] = True
                inDeg[lastRank[j]] += 1

        M = int(input().strip())
        for _ in range(M):
            a, b = map(int, input().strip().split())
            if graph[a][b]:
                inDeg[b] -= 1
                inDeg[a] += 1
            else:
                inDeg[a] -= 1
                inDeg[b] += 1
            graph[a][b], graph[b][a] = graph[b][a], graph[a][b]

        rtn = []
        ans = tsort()

        if ans:
            if len(rtn) == N:
                print(*rtn)
            else:
                print("IMPOSSIBLE")
        else:
            print("?")
