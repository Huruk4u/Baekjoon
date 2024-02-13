# 22/08/26
import sys

n = int(sys.stdin.readline().strip())
word = []
for _ in range(n):
    word.append(sys.stdin.readline().strip())

cnt = 0
for w in word:
    stack = []
    for s in w:
        if stack and (stack[-1] == s):
            stack.pop()
        else:
            stack.append(s)
    if not stack:
        cnt += 1

print(cnt)