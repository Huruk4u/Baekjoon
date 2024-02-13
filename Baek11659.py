import sys

# input
n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

# prefix_sum
prefix_sum = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

# solve
for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())

    print(prefix_sum[j] - prefix_sum[i-1])
    