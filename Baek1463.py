import sys

n = int(sys.stdin.readline().strip())

f = [0]*(n+1)

for i in range(2,n+1) :
    f[i] = f[i-1] + 1 #3
    if i%2 == 0:
        f[i] = min(f[i],f[i//2] + 1) # 2 vs 3
    if i%3 == 0: #
        f[i] = min(f[i],f[i//3] + 1)

print(f[n])