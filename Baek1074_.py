import sys

n,r,c = map(int,sys.stdin.readline().strip().split(" "))

res = 0
cnt = 0
s = (2**n)

def z(x,y,size) :
    global res, r, c, cnt

    if size<=1 :
        for col in range(x, x+size) :
            for row in range(y, y+size) :
                if col == c and row == r :
                    cnt = res
                res += 1
        return
    else :
        if c < (size//2) + x and r < (size//2) + y :
            z(x,y,size//2)

        elif c >= (size//2) + x and r < (size//2) + y :
            res += int((size**2)*0.25)
            z(x+(size//2), y, size//2)

        elif c < (size//2) + x and r >= (size//2) + y :
            res += int((size**2)*0.5)
            z(x, y+(size//2), size//2)

        else :
            res += int((size**2)*0.75)
            z(x+(size//2), y+(size//2), size//2)

z(0,0,s)
print(cnt)