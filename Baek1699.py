import sys

n = int(sys.stdin.readline().strip())

square=[]
for s in range(1,n):
    a=s*s
    if a > n : break
    square.append(a)
dp = [i for i in range(n+1)]

for i in range(1,n+1):
    for j in range(len(square) - 1, 0, -1):
        sqr = square[j]
        if i >= sqr :
            dp[i] = min(dp[i-1]+1,dp[i-sqr]+1,dp[i])
print(dp[n])