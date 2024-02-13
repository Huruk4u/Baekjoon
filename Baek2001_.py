import sys
from collections import deque

input = sys.stdin.readline


def bfs(queue):
    curr, state, weight = queue[0]
    vst[curr][state] = 1
    while queue:
        curr, state, weight = queue.popleft()
        weight_node[curr] = max(weight_node[curr], weight)
        k = 0
        if curr in idx_jewel:
            k = idx_jewel.index(curr)
            if state & (1 << k) == 0:
                weight_node[curr] = max(weight_node[curr], weight+1)
            else:
                k = 0

        for next, edge_weight in graph[curr]:
            # 줍지 않고 방문
            if weight <= edge_weight:
                if not vst[next][state]:
                    queue.append([next, state, weight])
                    vst[next][state] = 1
            # 주운 채로 방문
            if weight + 1 <= edge_weight:
                if k and not vst[next][state | (1 << k)]:
                    queue.append([next, state | (1 << k), weight+1])
                    vst[next][state | (1 << k)] = 1

    return weight_node[1]


if __name__ == '__main__':
    # input
    node, edge, jewel = map(int, input().strip().split())
    idx_jewel = [0]
    for _ in range(jewel):
        idx = int(input().strip())
        idx_jewel.append(idx)
    # print(idx_jewel)
    graph = [[] for _ in range(node+1)]
    for _ in range(edge):
        a, b, w = map(int, input().strip().split())
        graph[a].append([b, w])
        graph[b].append([a, w])

    # visit
    vst = [[0] * (1 << 15) for _ in range(node+1)]
    # queue
    q = deque()
    q.append([1, 0, 0])
    # weight_node
    weight_node = [0] * (node+1)

    print(bfs(q))
