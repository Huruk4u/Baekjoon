import sys

n = int(sys.stdin.readline().strip())
hist = [int(sys.stdin.readline().strip()) for _ in range(n)]

def wide(left, right) :
    if left == right : # 최소 단위로 분할되면 넓이 반환
        return hist[left]

    mid = (left+right)//2

    divWide = max(wide(left,mid),wide(mid+1,right))

    while