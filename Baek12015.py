import sys
input = sys.stdin.readline


def bs(num):
    low = 0
    high = len(lis) - 1
    while low <= high:
        mid = (low + high) // 2
        if lis[mid] == num:
            return mid

        if lis[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    return low


if __name__ == '__main__':
    N = int(input().strip())
    A = list(map(int, input().strip().split()))

    lis = [A[0]]

    for i in range(1, N):
        if lis[-1] < A[i]:
            lis.append(A[i])
        else:
            lis[bs(A[i])] = A[i]

    print(len(lis))
