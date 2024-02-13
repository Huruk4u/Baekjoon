# 22/08/13
import sys
from collections import deque

n,k = map(int,sys.stdin.readline().strip().split())
paper = []
for _ in range(k):
    a,b = sys.stdin.readline().strip().split()
    a = int(a)
    paper.append([a, b])

ans = deque(["?"] * n)

for turn,s in paper:
    ans.rotate(turn)
    if ans[0] != "?":
        if ans[0] != s:
            ans = ["!"]
            break
        else :
            continue
    else :
        if s in ans:
            ans = ["!"]
            break
        else :
            ans[0] = s

print("".join(ans))