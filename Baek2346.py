# 22/08/11
import sys,collections

n = int(sys.stdin.readline().strip())
arr = collections.deque(list(enumerate(map(int,sys.stdin.readline().strip().split()))))
res = []

temp = 0
right = 1

while arr:
    if len(arr) == 1:
        idx, temp = arr[0]
        res.append(idx+1)
        break
    if temp == 0:
        idx, temp = arr[0]
        if temp > 0:
            right = 1
        else:
            right = 0
        temp = abs(temp)
        res.append(idx+1)
        arr.popleft()
        if right == 0:
            arr.appendleft(arr[-1])
            arr.pop()
        temp -= 1
    else:
        if right:
            arr.append(arr[0])
            arr.popleft()
            temp -= 1
        else:
            arr.appendleft(arr[-1])
            arr.pop()
            temp -= 1

print(" ".join(str(i) for i in res))