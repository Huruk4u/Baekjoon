import sys

k,n = map(int,sys.stdin.readline().split(' '))
listK = [int(sys.stdin.readline()) for i in range(k)]

left = 1
right = max(listK)

while left<=right:
    midle = int((left+right)/2)
    res = 0
    for i in listK :
        res += i//midle

    if res < n :
        right = midle-1
    else :
        left = midle + 1
print(right)