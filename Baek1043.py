import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    if is_truth[root_x]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
    return


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    truth = list(map(int, input().strip().split()))
    is_truth = [False] * (N+1)
    if truth[0]:
        for i in range(1, truth[0] + 1):
            is_truth[truth[i]] = True

    party_list = []
    parent = [i for i in range(N+1)]
    for _ in range(M):
        party = list(map(int, input().strip().split()))
        if party[0] >= 2:
            for i in range(2, party[0] + 1):
                union(party[i-1], party[i])
        party_list.append(party)

    ans = 0
    for p in party_list:
        root_p = find(p[1])
        if is_truth[root_p]:
            continue
        else:
            ans += 1

    print(ans)
