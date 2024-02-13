import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    dp = [[0] * (N+1) for _ in range(N+1)]
    trian = []
    for _ in range(N):
        ipt = list(map(int, input().strip().split()))
        trian.append(ipt)
    trian.append([0] * (N+1))

    for lev in range(N-1, -1, -1):
        for i in range(len(trian[lev])):
            dp[lev][i] = max(dp[lev+1][i], dp[lev+1][i+1]) + trian[lev][i]

    print(dp[0][0])
