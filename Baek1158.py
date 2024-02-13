# 22/08/10
import sys, collections

n,k = map(int,sys.stdin.readline().strip().split())

arr = collections.deque([i for i in range(1,n+1)])
res = []
cooldown = k

while arr:
    if len(arr) == 1 :
        res.append(arr[0])
        break
    if cooldown == 0:
        cooldown = k
    else:
        cooldown -= 1
        # k번째 턴이 되면, pop
        if cooldown == 0:
            res.append(arr[0])
            arr.popleft()
        else:
            arr.append(arr[0])
            arr.popleft()

print("<",', '.join(str(_) for _ in res),">",sep="")