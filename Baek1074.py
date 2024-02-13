import sys

n,r,c = map(int,sys.stdin.readline().strip().split(" "))

res = 0
cnt = 0
s = (2**n)

def z(x,y,size) :
    global res, r, c, cnt
    # size가 최소단위에 도달하면 return.
    print(size)
    if size<=1 :
        for col in range(x, x+size) :
            for row in range(y, y+size) :
                print("res + 1 : RES = %d"%(res))
                print("%d : %d, %d : %d"%(col,c,row,r))
                if col == c and row == r :
                    cnt = res
                res += 1
        return
    else :
        # 구간 추적.
        print(c, r)
        print(size//2 +x, size//2+y )
        if c < (size//2) + x and r < (size//2) + y : # area 1.
            print("divide to area 1 ----------\nres = %d" % (res))
            z(x,y,size//2)

        elif c >= (size//2) + x and r < (size//2) + y : # area 2.
            res += (size**2)*0.25
            print("divide to area 2 ----------\nres = %d"%(res))

            z(x+(size//2), y, size//2)
        elif c < (size//2) + x and r >= (size//2) + y : # area 3.
            res += (size**2)*0.5

            print("divide to area 3 ----------\nres = %d"%(res))
            z(x, y+(size//2), size//2)
        else : # area 4.
            res += (size**2)*0.75

            print("divide to area 4 ----------\nres = %d" % (res))
            z(x+(size//2), y+(size//2), size//2)

z(0,0,s)
print(int(cnt))