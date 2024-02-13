import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    date = list(map(int, input().strip().split()))

    prefix_sum = [0] * (N+1)
    for i in range(1, N+1):
        prefix_sum[i] = prefix_sum[i-1] + date[i-1]

    ans = prefix_sum[K] - prefix_sum[0]
    for i in range(K+1, N+1):
        ans = max(ans, prefix_sum[i] - prefix_sum[i-K])

    print(ans)
