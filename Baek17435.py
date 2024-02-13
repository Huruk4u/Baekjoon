import sys
input = sys.stdin.readline


if __name__ == '__main__':
    m = int(input().strip())

    # dp[depth][x]
    f = [[0] * (m + 1) for _ in range(19)]
    f[0] = [0] + list(map(int, input().strip().split()))

    # dp
    for d in range(1, 19):
        for x in range(1, m + 1):   # 1 ~ m
            f[d][x] = f[d-1][f[d-1][x]]

    Q = int(input().strip())
    for _ in range(Q):
        n, x = map(int, input().strip().split())
        for i in range(18, -1, -1):
            if n < (1 << i):
                continue
            n -= (1 << i)
            x = f[i][x]

        print(x)
