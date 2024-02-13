import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    prefix_sum = [0] * (n+1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

    ans = -1000
    for i in range(1, n+1):
        for j in range(i):
            ans = max(ans, prefix_sum[i] - prefix_sum[j])

    print(ans)