import sys


def solve(idx, last, used, test):
    # exit point
    if idx == n-1:
        if used == (1 << 10) - 1:
            return 1
        return 0

    if dp[idx][last][used]:
        return dp[idx][last][used]

    if last == 0:
        dp[idx][last][used] += solve(idx+1, last+1, used | (1 << last+1), test+[last+1]) % mod
    elif last == 9:
        dp[idx][last][used] += solve(idx+1, last-1, used | (1 << last-1), test+[last-1]) % mod
    else:
        dp[idx][last][used] += solve(idx+1, last-1, used | (1 << last-1), test+[last-1]) % mod
        dp[idx][last][used] += solve(idx+1, last+1, used | (1 << last+1), test+[last+1]) % mod

    return dp[idx][last][used]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    # vst[현재 idx][사용한 숫자][가장 최근에 사용한 숫자]
    dp = []
    for _ in range(n+1):
        dp.append([[0] * (1 << 10) for _ in range(10)])

    mod = 1000000000

    ans = 0
    for i in range(1, 10):
        ans += solve(0, i, 1 << i, [i]) % mod

    print(ans % mod)
