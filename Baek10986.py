import sys

input = sys.stdin.readline

# input
n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

# 1,000,000
prefix_sum = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

# 1,000,000
for i in range(1, n+1):
    prefix_sum[i] %= m

# 1,000,000
rmd = [0] * m
for i in range(1, n+1):
    rmd[prefix_sum[i]] += 1

# 1,000
cnt = 0
for i in range(m):
    # if i = 0, rC1 + rC2
    if i == 0:
        cnt += rmd[i]
    cnt += (rmd[i] * (rmd[i]-1))//2

print(cnt)
