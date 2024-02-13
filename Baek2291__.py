import sys
input = sys.stdin.readline


def rtn_dp():
    for i in range(1, N+1):
        for j in range(1, M+1):
            # n이 m보다 큰 경우는 없음
            if i > j:
                continue
            # n이 1이면 경우의 수는 하나밖에 없음
            if i == 1:
                dp[i][j][j//i] = 1
                continue
            # f = 첫번째 칸 숫자
            for f in range(1, (j // i) + 1):
                # t = dp[i-1][j-f]의 첫번째 칸 숫자
                for t in range(f, len(dp[i-1][j-f])):
                    dp[i][j][f] += dp[i-1][j-f][t]


def solve(i, j, k, prev):
    remove = 0  # 제낄 순서
    pivot = 0   # k랑 비교할 거

    if i == 1:
        rtn.append(j)
        return
    for f in range(prev, (j//i) + 1):
        pivot += dp[i][j][f]
        if k <= pivot:
            # solve(i, j, k) = "f" + solve(i-1, j-f, k-remove)
            rtn.append(f)
            # 부분 케이스의 k번째 순서는 f 이전 경우의 수를 모두 제거한 k-remove번째 순서
            solve(i-1, j-f, k-remove, f)
            return
        else:
            remove += dp[i][j][f]
    return


if __name__ == '__main__':
    N, M, K = map(int, input().strip().split())

    # dp[n][m][f] = 합이 m인 n길이 수열 중 앞자리가 f인 수열의 개수
    dp = [[[0] for _ in range(M+1)] for _ in range(N+1)]
    for n in range(1, N+1):
        for m in range(1, M+1):
            for _ in range(1, (m//n)+1):
                dp[n][m].append(0)
    # dp 반환
    rtn_dp()

    # solve
    rtn = []
    solve(N, M, K, 1)

    print(*rtn)
