import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize


def beer_cost(cx, cy, nx, ny):
    dist = abs(ny - cy) + abs(nx - cx)
    if dist % 50 == 0:
        rtn = dist // 50
    else:
        rtn = (dist // 50) + 1

    return rtn


def is_happy():
    queue = deque([0])
    while queue:
        c = queue.popleft()
        cx, cy = node[c]
        vst[c] = True
        print("---------------------------------------------")
        print("현재 위치 (%d, %d)" % (cx, cy))
        if c == N+1:
            return True
        for i in range(N+2):
            print(i)
            if vst[i]:
                continue
            nx, ny = node[i]
            cost_i = beer_cost(cx, cy, nx, ny)
            print("to (%d, %d) 필요한 맥주의 개수 : %d" % (nx, ny, cost_i))
            # 편의점까지 가기 위해 필요한 맥주의 개수가 현재 가지고 있는 맥주의 개수보다 많을 경우 continue
            if cost_i > 20:
                continue
            queue.append(i)
            print()

    return False


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())

        node = [[0, 0] for _ in range(N+2)]
        node[0] = list(map(int, input().strip().split()))
        for _ in range(1, N+1):
            node[_] = list(map(int, input().strip().split()))
        node[N+1] = list(map(int, input().strip().split()))

        print(node)
        vst = [False] * (N+2)

        if is_happy():
            print("happy")
        else:
            print("sad")

