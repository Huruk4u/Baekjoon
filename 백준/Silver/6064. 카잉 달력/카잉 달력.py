import sys
import math
input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        M, N, x, y = map(int, input().strip().split())
        last_year = math.lcm(M, N)

        set_x, set_y = set(), set()
        for i in range(x, last_year + 1, M):
            set_x.add(i)
        for i in range(y, last_year + 1, N):
            set_y.add(i)

        answer = set_x.intersection(set_y)
        if not answer: print(-1)
        else:
            answer = answer.pop()
            print(answer)
