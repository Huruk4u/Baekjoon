import sys
input = sys.stdin.readline


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        a, d, x = map(int, input().strip().split())
        left, right = 1, x
        step = 1
        while left < right:
            mid = (right + left) // 2

            total = (mid * (2 * a + (mid - 1) * d)) // 2
            if x <= total:
                right = mid
                step = mid
            else:
                left = mid + 1

        start = ((step - 1) * (2 * a + (step - 2) * d)) // 2 + 1
        print(step, x - start + 1)
