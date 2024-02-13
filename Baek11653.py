import sys

a = int(sys.stdin.readline().strip())
sosu = []

for i in range(2,a+1) :
    count = 0
    if a%i == 0 :
        count+=1
    if count == 1 :
        sosu.append(i)

sosu.sort()

for s in sosu :
    while a%s==0 :
        a/=s
        print(s)

"""for i in range(1,a+1) :
    if a%i == 0 :
        a /= i
        print(i)"""