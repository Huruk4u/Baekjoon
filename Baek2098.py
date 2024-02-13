import sys


def solve(curr, vst):
    print("------------- %d visited --------------" % curr)
    print("state -> ", bin(vst))
    # all node visited
    if vst == (1 << n)-1:
        print("return %d" % weight[curr][0])
        return weight[curr][0]

    for i in range(1, n):
        # if not visited i
        if not vst & (1 << i):
            dp[curr][vst] = min(dp[curr][vst], solve(i, vst | (1 << i)) + weight[curr][i])
            print("dp %d %d = %d" % (curr, vst, dp[curr][vst]))

    return dp[curr][vst]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    weight = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    dp = [[10000000001] * ((1 << n) - 1) for _ in range(n)]

    print(solve(0, 1))
