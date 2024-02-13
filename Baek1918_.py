# 22/08/24
import sys

ipt = sys.stdin.readline().strip()
stack = []
res = []

for i in range(len(ipt)):
    if 'A' <= ipt[i] <= 'Z':
        res.append(ipt[i])
    else:
        if ipt[i] == '+' or ipt[i] == '-':
            while stack and stack[-1] != '(':
                res.append(stack.pop())
            stack.append(ipt[i])
        elif ipt[i] == '*' or ipt[i] == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res.append(stack.pop())
            stack.append(ipt[i])
        elif ipt[i] == '(':
            stack.append(ipt[i])
        elif ipt[i] == ')':
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                res.append(stack.pop())

while stack:
    res.append(stack.pop())

print(''.join(res))