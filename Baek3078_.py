# 22/08/30
import sys
from collections import deque
n,k = map(int,sys.stdin.readline().strip().split())

student = deque()
len_name = {i:0 for i in range(2,21)}
cnt = 0

for i in range(n):
    std = len(sys.stdin.readline().strip())
    student.append(std)
    if i>k:
        len_name[student.popleft()] -= 1
    cnt += len_name[std]
    len_name[std] += 1

print(cnt)