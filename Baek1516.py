import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())

    graph = [[] for _ in range(N+1)]
    inDeg = [0 for _ in range(N+1)]
    build_time = [0 for _ in range(N+1)]
    prepare_time = [0 for _ in range(N+1)]

    # N^2 = 250000
    for i in range(1, N+1):
        ipt = list(map(int, input().strip().split()))
        build_time[i] = ipt[0]
        for j in range(1, len(ipt) - 1):
            graph[ipt[j]].append(i)
            inDeg[i] += 1

    # inDeg = 0 인 노드부터 시작
    queue = deque([])
    for i in range(1, N+1):
        if not inDeg[i]:
            queue.append(i)

    rtn = [0 for _ in range(N+1)]
    while queue:
        curr = queue.popleft()
        rtn[curr] = build_time[curr] + prepare_time[curr]
        for next in graph[curr]:
            inDeg[next] -= 1
            prepare_time[next] = max(rtn[curr], prepare_time[next])
            if not inDeg[next]:
                queue.append(next)

    for i in range(1, N+1):
        print(rtn[i])
