import sys

def score(col,stat) :
    global n

    if col == n : return 0
    if f[col][stat] != -1 : return f[col][stat]

    res = score(col+1,0) # 아무것도 선택하지 않음
    if stat != 1:
        res = max(res, score(col+1,1) + value[0][col]) # 3 vs 1
    if stat != 2:
        res = max(res, score(col+1,2) + value[1][col]) # 3 vs 2
    f[col][stat] = res
    return res

T = int(sys.stdin.readline().strip())

for _ in range(T) :
    n = int(sys.stdin.readline().strip())
    value = [list(map(int,sys.stdin.readline().strip().split())) for x in range(2)]
    status = [-1,-1,-1]
    f = []
    for j in range(n):
        f.append(status)

    print(score(0,0))