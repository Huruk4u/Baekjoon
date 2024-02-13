import sys

input = sys.stdin.readline

T = int(input().strip())

# O(T)
for _ in range(T):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    # O(n)
    prefix_sum = [0] * (n+1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

    print(prefix_sum)
    # O(n^2)
    ans = -100000000000
    for i in range(1, n+1):
        for j in range(0, i):
            print("")
            print("i = %d, j = %d" % (i, j))
            print("prefix_sum[i] = %d, prefix_sum[j-1] = %d" % (prefix_sum[i], prefix_sum[j]))
            ans = max(ans, prefix_sum[i] - prefix_sum[j])

    print(ans)