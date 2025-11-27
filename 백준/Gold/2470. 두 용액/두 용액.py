import sys

input = sys.stdin.readline
INF = sys.maxsize

if __name__ == '__main__':
    N = int(input().strip())
    A = sorted(list(map(int, input().strip().split())))

    s, e = 0, N-1
    temp = INF
    answer_left, answer_right = 0, 0
    while s < e:
        if abs(A[s] + A[e]) < temp:
            answer_left, answer_right = A[s], A[e]
            temp = abs(A[s] + A[e])
            if temp == 0:
                break

        if A[s] + A[e] < 0:
            s += 1
        elif A[s] + A[e] > 0:
            e -= 1

    print(answer_left, answer_right)
