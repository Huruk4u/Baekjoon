import sys
input = sys.stdin.readline


def solve(curr):
    visited[curr] = 1
    dp[curr][1] = weight[curr]
    node[curr][1].append(curr)

    for child in tree[curr]:
        if visited[child]:
            continue
        path = solve(child)
        dp[curr][0] += max(dp[child][0], dp[child][1])      # 현재 노드를 선택하지 않는 경우의 최대 독립집합
        dp[curr][1] += dp[child][0]                         # 현재 노드를 선택하는 경우의 최대 독립집합

        node[curr][1] += path[0]    # 현재노드르 선택하는 경우 자식 노드를 선택하지 않는 경우의 경로를 추가함
        if dp[child][0] > dp[child][1]: # 현재노드를 선택하지 않는 경우 dp가 더 큰 경우의 경로를 추가함
            node[curr][0] += path[0]
        else:
            node[curr][0] += path[1]

    return node[curr]


if __name__ == '__main__':
    # input
    N = int(input().strip())
    weight = [0] + list(map(int, input().strip().split()))
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().strip().split())
        tree[a].append(b)
        tree[b].append(a)

    # dp[idx][selected] = 현재 idx를 포함하는지의 여부에 따른 최대 독립집합의 가중치
    dp = [[0, 0] for _ in range(N+1)]
    # 최대 독립집합의 노드 저장
    node = [[[], []] for _ in range(N+1)]
    visited = [0] * (N+1)

    solve(1)

    if dp[1][0] <= dp[1][1]:
        print(dp[1][1])
        print(*sorted(node[1][1]))
    else:
        print(dp[1][0])
        print(*sorted(node[1][0]))

