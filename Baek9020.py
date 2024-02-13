import sys

def primeFilter(n) :
    prime = [False,False] + [True]*(n-1)

    for i in range(2,int(n**0.5)+1) :
        if prime[i] :
            for j in range(2*i,n+1,i) :
                prime[j] = False

    isPrime = [x for x in range(n) if prime[x]]
    return isPrime

T = int(sys.stdin.readline().strip())

for t in range(T) :
    n = int(sys.stdin.readline().strip())
    primeList = primeFilter(n)
    x = [x for x in primeList if x <= n//2]
    for i in range(len(x)-1,-1,-1) :
        j = n-x[i]
        if j in primeList :
            if j > x[i] :
                print(f"{x[i]} {j}")
                break
            else :
                print(f"{j} {x[i]}")
                break