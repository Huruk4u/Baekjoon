import sys

def prime(a,b) :
    _prime = [False,False] + [True] * (b-1)
    for i in range(2,int(b**0.5)+1) :
        if _prime[i] == True :
            for j in range(i*2,b+1,i) :
                _prime[j] = False
    return [n for n in range(a,b+1) if _prime[n] == True]

m,n = map(int,sys.stdin.readline().split(' '))
res = prime(m,n)

for m in res :
    print(m)