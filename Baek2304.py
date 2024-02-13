# 22/08/25
import sys
n = int(sys.stdin.readline().strip())
pillar = [0]*1001
max_height = 0
high_locate = 0
max_locate = 0
for _ in range(n):
    locate, height = map(int,sys.stdin.readline().strip().split())
    pillar[locate] = height
    if height > max_height:
        max_height = height
        high_locate = locate
    if locate > max_locate:
        max_locate = locate

print(pillar)
stack = [0]
res = 0

for i in range(high_locate+1):
    print("=======================\nindex is = %d"%(i))
    if stack[-1] < pillar[i]:
        stack.append(pillar[i])
    print("stack is ",stack)
    res += stack[-1]
    print("res is %d"%(res))
stack = [0]
for i in range(max_locate,high_locate, -1):
    print("=======================\nindex is = %d"%(i))
    if stack[-1] < pillar[i]:
        stack.append((pillar[i]))
    print("stack is ",stack)
    res += stack[-1]
    print("res is %d"%(res))

print(res)