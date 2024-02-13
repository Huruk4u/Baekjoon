import sys

n = int(sys.stdin.readline().strip())
arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
quard = ""

def enc(x,y,n) :
    global arr, quard
    check = arr[x][y]

    for r in range(x,x+n) :
        for c in range(y,y+n) :
            if arr[r][c] != check:
                subquard = "(%s%s%s%s)"%(enc(x,y,n//2),enc(x,y+n//2,n//2)
                                             ,enc(x+n//2,y,n//2),enc(x+n//2,y+n//2,n//2))
                return quard+subquard

    if check == 1:
        return "1"
    else :
        return "0"

print(enc(0,0,n))