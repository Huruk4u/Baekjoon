import sys
input = sys.stdin.readline
INF = sys.maxsize


def score_cal(pick):
    pick_score, not_pick_score = 0, 0
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if pick[i] and pick[j]:
                pick_score += ability[i][j]
            elif not pick[i] and not pick[j]:
                not_pick_score += ability[i][j]

    return abs(pick_score - not_pick_score)


def backTracking(curr, depth):
    global answer
    if depth == N-1:
        return score_cal(pick)

    rtn = INF

    pick[curr + 1] = True
    rtn = min(rtn, backTracking(curr + 1, depth + 1))

    pick[curr + 1] = False
    rtn = min(rtn, backTracking(curr + 1, depth + 1))

    return rtn


if __name__ == '__main__':
    N = int(input().strip())
    ability = [list(map(int, input().strip().split())) for _ in range(N)]

    pick = [0 for _ in range(N)]
    print(backTracking(0, 0))
