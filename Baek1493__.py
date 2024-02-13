import sys
import math
sys.setrecursionlimit(30000)

l, w, h =  map(int,sys.stdin.readline().strip().split())
n = int(sys.stdin.readline().strip())
cubes = [0] * 21

for _ in range(n) :
    a,b = map(int,sys.stdin.readline().strip().split())
    cubes[a] = b

cnt = 0
a = 1<<20

fail = False
def div(l,w,h) :
    global cnt, fail
    # 정복
    if l <= 0 or w <= 0 or h <= 0 :
        return 0
    # 분할
    else :
        ln = min(min(l,w,h),a)
        ln_idx = int(math.log2(ln))
        for i in range(ln_idx,-1,-1) :
            if cubes[i] > 0 :
                cSize = 1 << i
                cubes[i] -= 1
                cnt += 1

                div(l - cSize, w, h) #1
                div(cSize, w- cSize, cSize) #2
                div(cSize, w, h-cSize) #3
                return
        fail = True
        return -1
div(l,w,h)

if fail == True :
    print(-1)
else : print(cnt)