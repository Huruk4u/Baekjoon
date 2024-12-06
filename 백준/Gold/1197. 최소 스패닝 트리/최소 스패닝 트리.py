import sys, heapq
sys.setrecursionlimit(1000000001)
input = sys.stdin.readline


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return False
    else:
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
        return True


if __name__ == '__main__':
    V, E = map(int, input().strip().split())

    parent = [i for i in range(V+1)]
    heap = []
    for i in range(E):
        u, v, w = map(int, input().strip().split())
        heapq.heappush(heap, (w, u, v))

    answer, cnt = 0, 0
    while heap and cnt < V-1:
        weight, u, v = heapq.heappop(heap)
        if union(u, v):
            answer += weight
            cnt += 1

    print(answer)
