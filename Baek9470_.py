import sys
from collections import deque
input = sys.stdin.readline


def start_node():
    rtn = deque([])
    for i in range(1, M+1):
        if not inDeg[i]:
            rtn.append(i)
            order[i] = 1

    return rtn


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        K, M, P = map(int, input().strip().split())

        graph = [[] for _ in range(M+1)]
        inDeg = [0 for _ in range(M+1)]
        order = [0 for _ in range(M + 1)]
        recentOrder = [0 for _ in range(M+1)]   # recentOrder[i] i번째 노드를 방문한 순서 중 가장 큰 순서

        for _ in range(P):
            a, b = map(int, input().strip().split())
            graph[a].append(b)
            inDeg[b] += 1

        queue = start_node()
        while queue:
            curr = queue.popleft()
            for next in graph[curr]:
                inDeg[next] -= 1

                if recentOrder[next] == order[curr]:
                    order[next] = max(order[curr] + 1, order[next])
                else:
                    order[next] = max(order[next], order[curr])
                    recentOrder[next] = max(order[curr], recentOrder[next])

                if not inDeg[next]:
                    queue.append(next)

        print(K, order[M])
