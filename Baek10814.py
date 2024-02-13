import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    queue = deque(tuple(map(str, input().strip().split())) for _ in range(N))

    # 200 * N
    sortedList = [deque([]) for _ in range(201)]
    # N
    while queue:
        age, name = queue.popleft()
        sortedList[int(age)].append(name)

    rtn = deque([])
    # 200 * N
    for i in range(1, 201):
        if not sortedList[i]:
            continue
        while sortedList[i]:
            rtn.append((i, sortedList[i].popleft()))

    for age, name in rtn:
        print(age, name)
