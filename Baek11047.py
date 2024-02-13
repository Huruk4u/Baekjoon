import sys

n,k = map(int,sys.stdin.readline().strip().split(' '))

price = sorted([int(sys.stdin.readline().strip()) for i in range(n)], reverse=True)
ans = 0

for p in price:
    if p <= k:
        ans += 1 * (k // p)
        k -= p*(k//p)

print(ans)