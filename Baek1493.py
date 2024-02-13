import sys

l, w, h =  map(int,sys.stdin.readline().strip().split(' '))
n = int(sys.stdin.readline().strip())

cubes = [list(map(int,sys.stdin.readline().strip().split(" "))) for i in range(n)]

box = l*w*h
cnt = 0

for i in range(n,0,-1) :
    print("\n Turn of cube ",cubes[i-1])
    for j in range(cubes[i-1][1]) :
        # 박스의 부피가 cube의 부피보다 크고, 큐브의 한 변이 모든 박스의 변보다 작을 때,
        if (box - (2**cubes[i-1][0])**3) >= 0 and min(l,w,h) >= (2**cubes[i-1][0]) :
            print("box = %d, cube = %d"%(box,(2**cubes[i-1][0])**3))
            box -= (2**cubes[i-1][0])**3
            cnt += 1
            print("cnt = ",cnt)
        else : continue
    if box == 0 : break

if box == 0 :
    print(cnt)
else : print(-1)