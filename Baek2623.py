import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    graph = [[] for _ in range(N+1)]
    inDeg = [0 for _ in range(N+1)]
    for _ in range(M):
        seq = list(map(int, input().strip().split()))
        for i in range(2, seq[0]+1):
            graph[seq[i-1]].append(seq[i])  # 이전 순서의 노드가 현재 순서의 노드로 진행할 수 있도록
            inDeg[seq[i]] += 1

    queue = deque([])
    rtn = []
    for i in range(1, N+1):
        if not inDeg[i]:
            rtn.append(i)
            queue.append(i)
            inDeg[i] = -1

    # solve
    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            inDeg[next] -= 1

        for i in range(1, N+1):
            if not inDeg[i]:
                rtn.append(i)
                queue.append(i)
                inDeg[i] = -1

    if len(rtn) == N:
        for i in range(N):
            print(rtn[i])
    else:
        print(0)
