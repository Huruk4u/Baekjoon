import sys

n,k = map(int,sys.stdin.readline().strip().split())

coin = []
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    coin.append(x)
coin.sort()

dp = [10001]*(k+1)
dp[0] = 0

for c in coin:
    for i in range(c,k+1):
        # 1 + f(n, k - value of coin)
        dp[i] = min(dp[i],dp[i-c] + 1)

if dp[k] == 10001:
    print(-1)
else : print(dp[k])