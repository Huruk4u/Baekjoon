# 22/08/24
import sys

n = int(sys.stdin.readline().strip())
ipt = str(sys.stdin.readline().strip())
var = []
for _ in range(n):
    var.append(int(sys.stdin.readline().strip()))
print(var)
res = 0
stack = []
for i in range(len(ipt)):
    print('=====================\nipt[i] is %s'%(ipt[i]))
    if ord('A') <= ord(ipt[i]) <= ord('Z'):
        stack.append(var[ord(ipt[i]) - ord('A')])
        print('append %d'%(var[ord(ipt[i]) - ord('A')]))
    else :
        second = stack.pop()
        first = stack.pop()
        if ipt[i] == '+':
            stack.append(first+second)
        elif ipt[i] == '-':
            stack.append(first-second)
        elif ipt[i] == '*':
            stack.append(first*second)
        elif ipt[i] == '/':
            stack.append(first/second)
    print(stack)

print("{:.2f}".format(stack[0]))