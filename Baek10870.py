import sys

n = int(sys.stdin.readline().strip())
fibo = []
for i in range(n+1) :
    if i <= 1 :
        fibo.append(i)
    else :
        fibo.append(fibo[i-2]+fibo[i-1])
print(fibo[-1])