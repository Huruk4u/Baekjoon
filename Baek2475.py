import sys

a = [i*i for i in map(int,sys.stdin.readline().split(' '))]

print(sum(a)%10)