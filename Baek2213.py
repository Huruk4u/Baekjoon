import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000001)


# idx = 현재 노드의 위치, able = 부모 노드의 선택 여부
def solve(idx, parent_selected):
    if dp[idx][parent_selected]:
        return dp[idx][parent_selected]

    visited[idx][parent_selected] = 1
    if parent_selected:  # 현재 노드를 선택할 수 없는 경우
        rtn = 0
        for child in tree[idx]:
            if visited[child][parent_selected]:
                print("%d visited" % child)
                continue
            rtn += solve(child, 0)
        print("%d %d rtn = %d" % (idx, parent_selected, rtn))
        dp[idx][parent_selected] = rtn
        print("%d %d return %d" % (idx, parent_selected, dp[idx][parent_selected]))
        return dp[idx][parent_selected]

    else:  # 현재 노드를 선택할 수 있는 경우
        rtn_0 = 0  # 현재 노드를 선택하지 않는 경우의 return
        rtn_1 = weight[idx]  # 현재 노드를 선택하는 경우의 return
        for child in tree[idx]:
            if visited[child][parent_selected]:
                continue
            rtn_0 += solve(child, 0)
            rtn_1 += solve(child, 1)

        print("rtn_0 = %d, rtn_1 = %d" % (rtn_0, rtn_1))

        if rtn_0 <= rtn_1:
            node_list.append(idx)
            weight_list.append(weight[idx])
            dp[idx][parent_selected] = rtn_1

        else:
            dp[idx][parent_selected] = rtn_0

        print("%d %d return %d" % (idx, parent_selected, dp[idx][parent_selected]))

        return dp[idx][parent_selected]


if __name__ == '__main__':
    # input
    N = int(input().strip())
    weight = [0] + list(map(int, input().strip().split()))
    tree = [[] for _ in range(N + 1)]
    tree[0].append(1)
    for _ in range(N - 1):
        a, b = map(int, input().strip().split())
        tree[a].append(b)
        tree[b].append(a)

    # dp[idx][able] = 노드가 idx인 노드의 서브트리, 선택 가능 여부에 따른 독립집합의 최대 가중치..?
    dp = [[0, 0] for _ in range(N + 1)]
    visited = [[0, 0] for _ in range(N + 1)]
    node_list = []
    weight_list = []
    print(solve(0, 0))
    print(node_list)
    print(weight_list)
    print(dp)
