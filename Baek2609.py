import sys

a,b = map(int,sys.stdin.readline().split(' '))

if a>b:
    n,m = a,b
else :
    m,n=a,b

while m!=0:
    n = n%m
    n,m = m,n

print(n)

print(a*b//n)