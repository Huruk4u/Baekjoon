import sys

n = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]

neg = zero = pos = 0

def finder(x,y,n):
    global neg, zero, pos
    check = paper[x][y]
    for i in range(x,x+n) :
        for j in range(y,y+n) :
            if paper[i][j] != check:
                for col in range(3) :
                    for row in range(3) :
                        finder(x+col*(n//3),y+row*(n//3),n//3)
                return

    if check == -1 :
        neg += 1
    elif check == 0 :
        zero += 1
    else :
        pos += 1

finder(0,0,n)
print("%d\n%d\n%d"%(neg,zero,pos))