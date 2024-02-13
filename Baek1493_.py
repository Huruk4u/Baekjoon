import sys

l, w, h =  map(int,sys.stdin.readline().strip().split(' '))
n = int(sys.stdin.readline().strip())

cubes = [0] * 21
for _ in range(n) :
    a,b = map(int,sys.stdin.readline().strip().split())
    cubes[a] = b

cnt = 0
boxsize = l*w*h

def div(l,w,h) :
    global boxsize, cnt
    print("L : %d, W : %d, H : %d, -- boxsize : %d"%(l,w,h,boxsize))
    box = l*w*h
    print("box = %d"%(box))
    # 정복
    if l <= 0 or w <= 0 or h <= 0 :
        print("return -----------------")
        return
    # 분할
    else :
        for i in range(n) :
            cSize = 2 ** cubes[i]
            if cubes[i] > 0 :
                print("-----------fill the cubes %d"%(cSize))
                cubes[i] -= 1
                print("cubes num : %d"%(cubes[i]))
                boxsize -= cSize**3
                print("boxsize is %d"%(boxsize))
                cnt += 1

                div(l - cSize, w, h) #1
                div(cSize, w- cSize, cSize) #2
                div(cSize, w, h-cSize) #3
                break
div(l,w,h)

if boxsize >= 1 :
    print(-1)
else : print(cnt)