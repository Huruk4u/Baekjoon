import sys

input = sys.stdin.readline

poketmon = dict()
number = dict()

n, m = map(int, input().strip().split())

for i in range(1, n+1):
    name = input().strip()
    poketmon[i] = name
    number[name] = i

for _ in range(m):
    q = input().strip()
    if q.isdigit():
        print(poketmon[int(q)])
    else:
        print(number[q])
