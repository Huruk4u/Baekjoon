# 22/08/23
import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    stack = []
    isVps = str(sys.stdin.readline().strip())
    err = False
    for i in range(len(isVps)):
        if isVps[i] == ')':
            if stack:
                stack.pop()
            else:
                err = True
                break
        else :
            stack.append(isVps[i])
    if not stack and err == False:
        print("YES")
    else:
        print("NO")