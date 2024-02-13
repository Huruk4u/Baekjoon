import sys

T = int(sys.stdin.readline())

for t in range(T) :
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split(' '))

    jo = (x1,y1)
    baek = (x2,y2)
    r = [r1,r2]
    betweenWide =abs(x1-x2)
    betweenHeight = abs(y1-y2)
    betweenDis = ((betweenWide**2) + (betweenHeight**2))**0.5

    if betweenDis < max(r) :
        if jo == baek :
            if r1 == r2 :
                print(-1)
            else : print(0)
        elif betweenDis + min(r) < max(r) :
            print(0)
        elif betweenDis + min(r) == max(r) :
            print(1)
        else :
            print(2)

    else :
        if r1+r2 > betweenDis :
            print(2)
        elif r1+r2 == betweenDis :
            print(1)
        else :
            print(0)