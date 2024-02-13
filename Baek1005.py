import sys
from collections import deque
input = sys.stdin.readline


def start_node():
    rtn = deque([])
    for i in range(1, N + 1):
        if not inDeg[i]:
            rtn.append(i)
    return rtn


def tsort(Q):
    queue = start_node()
    rtn = [0 for _ in range(N + 1)]
    # 1000
    while queue:
        curr = queue.popleft()
        rtn[curr] = buildTime[curr] + prepareTime[curr]
        if curr == Q:
            return rtn[curr]

        for next in graph[curr]:
            prepareTime[next] = max(prepareTime[next], rtn[curr])
            inDeg[next] -= 1
            if not inDeg[next]:
                queue.append(next)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N, K = map(int, input().strip().split())
        graph = [[] for _ in range(N+1)]
        inDeg = [0 for _ in range(N+1)]

        buildTime = [0] + list(map(int, input().strip().split()))
        prepareTime = [0 for _ in range(N+1)]

        for _ in range(K):
            a, b = map(int, input().strip().split())
            graph[a].append(b)
            inDeg[b] += 1

        Q = int(input().strip())
        rtn = tsort(Q)

        print(rtn)
