import sys

n = int(sys.stdin.readline().strip())

list1 = sorted([int(sys.stdin.readline().strip()) for i in range(n)])

for j in list1 :
    print(j)