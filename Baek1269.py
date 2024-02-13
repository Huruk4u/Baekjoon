import sys

input = sys.stdin.readline

na, nb = map(int, input().strip().split())
a = set(map(int, input().strip().split()))
b = set(map(int, input().strip().split()))

print(len(a-b) + len(b-a))
