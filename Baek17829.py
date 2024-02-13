import sys

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]

def kongkong(x,y,n) :
    # n이 최소 단위에 도달했을 때, return 값은 두 번째로 큰 수
    if n <= 2:
        twotwo = []
        for col in range(x,x+n) :
            for row in range(y, y+n) :
                twotwo.append(arr[col][row])
        twotwo.sort()
        return twotwo[-2]
    # n이 최소 단위에 도달하지 않으면 분할.
    else :
        res = []
        res.append(kongkong(x,y,n//2)) #1
        res.append(kongkong(x+n//2,y,n//2)) #2
        res.append(kongkong(x,y+n//2,n//2)) #3
        res.append(kongkong(x+n//2,y+n//2,n//2)) #4
        res.sort()

        return res[-2]

print(kongkong(0,0,n))