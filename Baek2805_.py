# 22/07/13
import sys

n,m = map(int,sys.stdin.readline().strip().split())
tree = list(map(int,sys.stdin.readline().strip().split()))
h = max(tree)

def finder(minh, maxh):
    if maxh-minh <= 1 :
        print(minh)
        return

    global m
    midh = (minh + maxh)//2
    total = 0

    for i in range(n):
        if tree[i] <= midh:
            continue
        else :
            total += tree[i] - midh

    if m > total: # 조건 미충족
        finder(minh,midh)
    else: # 조건 충족
        finder(midh,maxh)

finder(0,h)