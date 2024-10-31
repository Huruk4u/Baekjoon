import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    # i번 과목을 수강하기 위해 제출해야 할 최소 마일리지
    needs = []
    for _ in range(N):
        g, cap = map(int, input().strip().split())
        mileage = sorted(list(map(int, input().strip().split())), reverse=True)

        min_mile = mileage[cap-1] if len(mileage) > cap-1 else 1
        needs.append(min_mile)

    needs.sort()
    temp, answer = 0, 0
    for m in needs:
        if temp + m > M:
            break
        temp += m
        answer += 1

    print(answer)
