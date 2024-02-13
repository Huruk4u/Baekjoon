import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
sosu = []

for i in range(a,b+1) :
    count = 0
    for n in range(1,i+1) :
        if i%n == 0 :
            count +=1
    if count == 2 :
        sosu.append(i)
if len(sosu) > 0 :
    print(sum(sosu))
    print(min(sosu))
else :
    print(-1)