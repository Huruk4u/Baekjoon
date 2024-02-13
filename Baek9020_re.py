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
    firP = [x for x in primeList if x<= int(n/2)]
    secP = [y for y in primeList if y>= int(n/2)]
    goldbach = []
    for x in firP :
        for y in secP :
            if x+y == n :
                goldbach.append([x,y])

    print("{0:n} {1:n}".format(goldbach[-1][0],goldbach[-1][1]))