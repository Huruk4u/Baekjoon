import sys
import heapq

N = int(sys.stdin.readline().strip())
mlist = []
croom = []
for _ in range(N):
    s,t = map(int,sys.stdin.readline().strip().split(' '))
    mlist.append([s,t])

mlist = sorted(mlist, key=lambda x:x[0])
heapq.heappush(croom,mlist[0][1]) # croom = [3]

for i in range(1,N):
    if croom[0] <= mlist[i][0] :
        heapq.heappop(croom)
        heapq.heappush(croom,mlist[i][1])
    else :
        heapq.heappush(croom,mlist[i][1])

print(len(croom))
