import sys

a,b,c = map(int,sys.stdin.readline().strip().split(' '))

def h4u(x,y):
    if y == 1:
        return x%c
    k = h4u(x,y//2)
    if y%2 == 1 :
        return (k*k*x)%c
    else :
        return (k*k)%c

print(h4u(a,b))