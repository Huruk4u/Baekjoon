import sys
input = sys.stdin.readline


def solve(i, color):
    if dp[i][color] != 1000000:
        print("return")
        return dp[i][color]
    # 마지막 집에 도달했을 때
    if i == N-1:
        print("마지막 집 도달 %d색 비용 %d" % (color, cost[i][color]))
        return cost[i][color]

    if color == 0:
        dp[i][color] = min(solve(i + 1, 1), solve(i + 1, 2)) + cost[i][color]
    elif color == 1:
        dp[i][color] = min(solve(i + 1, 0), solve(i + 1, 2)) + cost[i][color]
    else:
        dp[i][color] = min(solve(i + 1, 0), solve(i + 1, 1)) + cost[i][color]
    print("---------------------------")
    print("%d 번째 집 %d 색으로 칠했을 때" % (i, color))
    print("비용은 %d" % dp[i][color])

    return dp[i][color]


if __name__ == '__main__':
    N = int(input().strip())
    cost = []
    for _ in range(N):
        cost.append(list(map(int, input().strip().split())))

    dp = [[1000000] * N for _ in range(N)]

    ans = 1000000
    for c in range(3):
        print("==============================")
        print("첫번째 집 %d 색" % c)
        ans = min(ans, solve(0, c))

    print(ans)
