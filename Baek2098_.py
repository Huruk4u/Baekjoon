import sys


def solve(curr, vst):
    global inf

    if vst == (1 << n)-1:
        if not weight[curr][0]:
            return inf
        else:
            return weight[curr][0]

    if dp[curr][vst] != -1:
        return dp[curr][vst]

    dist = inf
    for i in range(1, n):
        if not weight[curr][i] or vst & (1 << i):
            continue
        dist = min(dist, solve(i, vst | (1 << i)) + weight[curr][i])

    dp[curr][vst] = dist

    return dp[curr][vst]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    weight = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

    inf = 100000001

    dp = [[-1] * (1 << n) for _ in range(n)]

    print(solve(0, 1))
