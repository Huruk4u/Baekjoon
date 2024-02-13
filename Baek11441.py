import sys

input = sys.stdin.readline

# input
n = int(input().strip())
arr = list(map(int, input().strip().split()))
m = int(input().strip())

prefix_sum = [0] * (n+1)
for idx in range(1, n+1):
    prefix_sum[idx] = prefix_sum[idx-1] + arr[idx-1]

for _ in range(m):
    i, j = map(int, input().strip().split())
    print(prefix_sum[j] - prefix_sum[i-1])
