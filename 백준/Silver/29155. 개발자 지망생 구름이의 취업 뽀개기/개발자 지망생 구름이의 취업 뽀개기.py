import sys, heapq
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    p = list(map(int, input().strip().split()))

    problem = [[] for _ in range(5)]
    for _ in range(N):
        level, t = map(int, input().strip().split())
        heapq.heappush(problem[level-1], t)

    answer = []
    for lev in range(5):
        for i in range(p[lev]):
            st = heapq.heappop(problem[lev])
            if i == 0:
                answer.append(60)
            else:
                answer.append(abs(answer[-1] - st))
            answer.append(st)

    answer.pop(0)
    print(sum(answer))
