import sys

n = int(sys.stdin.readline().strip())

dp = [1,2]

for i in range(2,n):
    a = (dp[i-1] + dp[i-2])%15746
    dp.append(a)

print(dp[n-1])