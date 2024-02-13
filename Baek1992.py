import sys

n = int(sys.stdin.readline().strip())
arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
quard = ""

def enc(x,y,n) :
    global arr, quard
    check = arr[x][y]
    print("----------------x : %d, y : %d, n: %d, check : %d -------------"%(x,y,n,check))
    # 모든 배열의 숫자가 check와 동일한가?
    for r in range(x,x+n) :
        for c in range(y,y+n) :
            # 동일하지 않으면 4분할
            if arr[r][c] != check:
                print("divide four in col : %d row : %d"%(c,r))
                subquard = "(%s%s%s%s)"%(enc(x,y,n//2),enc(x,y+n//2,n//2)
                                             ,enc(x+n//2,y,n//2),enc(x+n//2,y+n//2,n//2))
                return quard+subquard

    if check == 1:
        print("Add 1")
        return "1"
    else :
        print("Add 0")
        return "0"

print(enc(0,0,n))