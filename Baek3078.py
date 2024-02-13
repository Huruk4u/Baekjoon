# 22/08/30
import sys
from collections import deque
n,k = map(int,sys.stdin.readline().strip().split())
student = deque()
for _ in range(n):
    student.append(sys.stdin.readline().strip())

cnt = 0
for i in range(n): # 0~n
    std = len(student[0])
    if k >= len(student):
        k = len(student)-1
    for j in range(1,k+1): # 0~k+1
        if std == len(student[j]):
            cnt += 1
    student.popleft()
print(cnt)