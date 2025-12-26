import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    durability = deque(list(map(int, input().strip().split())))
    robots = deque([False for _ in range(N*2)])

    temp, cnt = 0, 1
    while True:
        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        durability.rotate()
        robots.rotate()
        if robots[N-1]: robots[N-1] = False

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
        for i in range(N-2, -1, -1):
            if not robots[i]: continue
            # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아있어야 한다.
            if durability[i+1] > 0 and not robots[i+1]:
                robots[i+1] = True
                durability[i+1] -= 1
                if not durability[i+1]: temp += 1
                robots[i] = False
                if i+1 == N-1:
                    robots[i+1] = False

        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if durability[0] > 0:
            durability[0] -= 1
            if not durability[0]: temp += 1
            robots[0] = True

        # 4. 내구도가 0인 칸의 갯수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면, 1번으로 돌아간다.
        if temp >= K:
            break

        cnt += 1


    print(cnt)
