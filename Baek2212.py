import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
sensor = sorted(map(int,sys.stdin.readline().strip().split(' ')))

dtn = []

while True :
    if k >= n :
        break
    for i in range(1,n) :
        dtn.append(sensor[i] - sensor[i-1])

    for j in range(k-1) :
        dtn.remove(max(dtn))
    break

print(sum(dtn))