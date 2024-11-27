import sys


def solution(distance, rocks, N):
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()

    left, right = 1, distance
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        flag, cnt = True, 0
        prev = 0
        for i in range(1, len(rocks)):
            dist = rocks[i] - rocks[prev]
            if dist < mid:
                cnt += 1
            else:
                prev = i

        if cnt > N:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer