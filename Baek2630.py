import sys

n = int(sys.stdin.readline().strip())
paper = [list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(n)]

zero = one = 0

def finder(x,y,n) :
    global zero, one
    check = paper[x][y]
    for a in range(x,x+n):
        for b in range(y,y+n):
            if check != paper[a][b]:
                finder(x,y,n//2) #1
                finder(x+n//2,y,n//2) #2
                finder(x,y+n//2,n//2) #3
                finder(x+n//2,y+n//2,n//2) #4
                return

    if check == 1:
        one += 1
    else : zero += 1
finder(0,0,n)
print("%d\n%d"%(zero,one))