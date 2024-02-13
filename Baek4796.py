import sys
i = 1
while True :
    l,p,v = map(int,sys.stdin.readline().strip().split(' '))
    if l == p == v == 0 :
        break

    ans = ((v//p)*l) + min(l,(v%p))

    print("Case {0:n}: {1:n}".format(i, ans))
    i += 1