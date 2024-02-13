# 22/08/10
import sys

n, k = map(int, sys.stdin.readline().strip().split())

arr = [i for i in range(1, n + 1)]
res = []
temp = k-1

while arr:
    if len(arr) == 1:
        res.append(arr[0])
        break
    if temp >= len(arr):
        temp = temp%len(arr)
        res.append(arr[temp])
        arr.pop(temp)
        temp += k-1
    else:
        res.append(arr[temp])
        arr.pop(temp)
        temp += k-1

print("<",', '.join(str(_) for _ in res),">",sep="")