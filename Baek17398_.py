import sys
input = sys.stdin.readline


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return
    else:
        parent[root_b] = root_a
        weight[root_a] += weight[root_b]


if __name__ == '__main__':
    N, M, Q = map(int, input().strip().split())

    edge = [[]]
    for _ in range(M):
        edge.append(list(map(int, input().strip().split())) + [1])

    edge_break = []
    for _ in range(Q):
        i = int(input().strip())
        edge_break.append(i)
        edge[i][2] = 0

    parent = [i for i in range(N+1)]    # 부모 노드 정보
    weight = [0] + [1 for _ in range(N)]    # 유니온의 크기

    # 초기 상태 설정
    for i in range(1, M):
        if edge[i][2]:
            a = edge[i][0]
            b = edge[i][1]
            union(a, b)

    # solve
    ans = 0
    while edge_break:
        i = edge_break.pop()
        a = edge[i][0]
        b = edge[i][1]

        # 서로 연결되어 있지 않은 상태
        if find(a) == b or find(b) == a:
            union(a, b)
            continue
        ans += (weight[parent[a]] * weight[parent[b]])
        union(a, b)

    print(ans)
