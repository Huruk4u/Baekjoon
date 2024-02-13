import sys

n = int(sys.stdin.readline().strip())

ss = res = 0

for i in range(n+1):
    ss += i
    for j in range(len(str(i))):
        ss += int(str(i)[j])
    if ss == n :
        res = i
        break
    ss = 0
print(res)