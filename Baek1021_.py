# 22/08/09
import sys
import collections

n,m = map(int,sys.stdin.readline().strip().split())
num_index = list(map(int,sys.stdin.readline().strip().split()))

q = collections.deque([i for i in range(1,n+1)])
cnt = 0

for num in num_index:
    if q[0] == num:
        q.popleft()
        continue
    else :
        if q.index(num) <= len(q)//2:
            while q[0] != num :
                q.append(q[0])
                q.popleft()
                cnt+=1
            q.popleft()
        else:
            while q[0] != num :
                q.appendleft(q[-1])
                q.pop()
                cnt+=1
            q.popleft()

print(cnt)