from sys import stdin

n = int(stdin.readline().strip())
res = 1
for n in range(2,n+1) :
    res *= n
print(res)