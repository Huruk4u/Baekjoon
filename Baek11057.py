import sys

n = int(sys.stdin.readline().strip())

dp = [[0]*10 for _ in range(n+1)]
for _ in range(10):
    dp[1][_] = 1

for i in range(2,len(dp)):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
res = sum(dp[n]) % 10007
print(res)