# 22/07/13
# 구하고자 하는 것 : 최소 m을 달성하는 최대 h

import sys

n,m = map(int,sys.stdin.readline().strip().split())
tree = list(map(int,sys.stdin.readline().strip().split()))

h = max(tree)

def finder(minh, maxh):
    print(minh, maxh, "-----------------")
    if maxh-minh <= 1 :
        print(minh)
        return
    global m
    midh = (minh + maxh)//2
    print("mid high = %d"%(midh))
    total = 0
# total tree high 계산
    for i in range(n):
        if tree[i] <= midh:
            print("트리가 너무 작아요")
            continue
        else :
            total += tree[i] - midh
            print("total update %d"%(total))

    if m > total: # 조건 미충족
        finder(minh,midh)
    else: # 조건 충족
        finder(midh,maxh)

finder(0,h)