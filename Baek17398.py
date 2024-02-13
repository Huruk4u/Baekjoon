import sys

ssr = sys.stdin.readline

N, M, Q = map(int, ssr().split())
root = [i for i in range(N + 1)]
graph = [list(map(int, ssr().split())) for _ in range(M)]
query = [int(ssr()) for _ in range(Q)]
weight = [1 for _ in range(N + 1)]

print(graph)
print(query)
print(weight)

def find(node):
    if root[node] != node:
        root[node] = find(root[node])
    return root[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    root[root2] = root1
    if root1 != root2:
        weight[root1] += weight[root2]


copied_query = list(query)
copied_query.sort()
query_point = 0
for i in range(M):
    if query_point < Q:
        if copied_query[query_point] == i + 1:
            query_point += 1
            continue
    union(graph[i][0], graph[i][1])
print("root", root)
ans = 0
for _ in range(Q):
    q = query.pop()
    n1, n2 = graph[q - 1]
    root1 = find(n1)
    root2 = find(n2)
    if root1 != root2:
        ans += weight[root1] * weight[root2]
        root[root2] = root1
        weight[root1] += weight[root2]
print(ans)