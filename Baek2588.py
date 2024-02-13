import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())

print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))
print(a*b)