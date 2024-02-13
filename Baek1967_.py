import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000001)


def max_route(curr):
    global ans

    left, right = tree[curr]
    # leaf node
    if not left and not right:
        return 0

    if left and right:
        left_route = weight[curr][0] + max_route(left)
        right_route = weight[curr][1] + max_route(right)
        ans = max(left_route + right_route, ans)
        return max(left_route, right_route)
    else:
        left_route = weight[curr][0] + max_route(left)
        ans = max(left_route, ans)
        return left_route


if __name__ == '__main__':
    n = int(input().strip())

    tree = [[0, 0] for _ in range(n+1)]
    weight = [[0, 0] for _ in range(n+1)]
    for _ in range(n-1):
        p, c, w = map(int, input().strip().split())
        if not tree[p][0]:
            tree[p][0] = c
            weight[p][0] = w
        else:
            tree[p][1] = c
            weight[p][1] = w

    ans = 0
    max_route(1)

    print(ans)
