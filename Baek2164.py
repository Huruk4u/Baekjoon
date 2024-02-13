import sys
from collections import deque

n = int(sys.stdin.readline().strip())
listN = deque()

for j in range(n) :
    listN.append(j+1)

i=0

while len(listN)>1:
   i+=1
   if i % 2 == 1:
       listN.popleft()
   elif i % 2 == 0:
       listN.append(listN.popleft())


print(listN[0])