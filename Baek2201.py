import sys
input = sys.stdin.readline


def rtn_dp():
    for i in range(1, 101):
        if i == 1:
            dp[i][1] = 1
        elif i == 2:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]

        dp_sum[i] = dp_sum[i-1] + dp[i][0] + dp[i][1]

    return


# solve(n, k) = n 자리의 이친수 중에서 k번째 수를 찾는다.
def solve(n, k):
    if n == 2:
        return ""
    if k <= (dp_sum[n-3] + 1):
        return "0" + solve(n-1, k)
    else:
        return "1" + solve(n-1, k - (dp_sum[n-3] + 1))


if __name__ == '__main__':
    K = int(input().strip())

    # dp[n][k] = n길이, 마지막 수가 k일 때 이친수의 개수
    dp = [[0, 0] for _ in range(101)]
    # dp_sum[n] = n길이로 만들 수 있는 이친수의 개수
    dp_sum = [0 for _ in range(101)]
    rtn_dp()

    # k번째 이친수의 자릿수를 구함
    n = 0
    for i in range(1, 101):
        if K <= dp_sum[i]:
            n = i
            break

    # solve
    if n == 1:
        print("1")
    else:
        print("10" + solve(n, K-dp_sum[n-1]))

    print(dp)
    print(dp_sum)