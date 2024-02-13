import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().strip().split(' ')))

def finder(s,e):
    mid = (s+e)//2
    LR = 0
    if s==e: return min(arr[s:e])*sum(arr[s:e])

    else :
        # left, right
        LR = max(finder(s,mid),finder(mid+1,e))
    ll = mid, rl = mid+1
    while ll>s or rl < e : # ll이 왼쪽 상한보다 크고 rl이 오른쪽 상한보다 작을 동안 루프
        if rl<e and(ll== s or arr[ll-1] > arr[rl+1]) :
            rl += 1
        else :
            ll -= 1
            