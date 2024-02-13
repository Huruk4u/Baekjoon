from sys import stdin

while True:
    n = int(stdin.readline())
    if n == 0 :
        break
    m = 2*n
    n += 1
    _prime = [False,False] + [True] * (m-1)
    def prime(n) :
        for i in range(2,int(m**0.5)+1) :
            if _prime[i] == True :
                for j in range(i*2,m+1,i) :
                    _prime[j] = False
        return [x for x in range(n,m+1) if _prime[x] == True]

    res = prime(n)
    print(len(res))