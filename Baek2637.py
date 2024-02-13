import sys
from collections import deque
input = sys.stdin.readline


def tsort():
    queue = deque([N])
    needs = [0 for _ in range(N + 1)]
    needs[N] = 1
    while queue:
        curr = queue.popleft()
        for next, weight in graph[curr]:
            needs[next] += (needs[curr] * weight)  # 필요한 현재 부품 개수 * 현재 부품을 만들기 위해 필요한 개수
            inDeg[next] -= 1
            if not inDeg[next]:
                queue.append(next)

    return needs


if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())

    graph = [[] for _ in range(N+1)]
    inDeg = [0 for _ in range(N+1)]
    outDeg = [0 for _ in range(N+1)]    # outDeg[i] = 0 -> 기본 부품

    for _ in range(M):
        x, y, k = map(int, input().strip().split())
        graph[x].append([y, k])
        inDeg[y] += 1
        outDeg[x] += 1

    rtn = tsort()
    for i in range(1, N):
        if not outDeg[i]:
            print(i, rtn[i])
