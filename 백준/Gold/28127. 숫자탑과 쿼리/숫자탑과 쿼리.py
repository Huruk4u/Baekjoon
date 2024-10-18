import sys
input = sys.stdin.readline


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        a, d, x = map(int, input().strip().split())
        left, right = 1, a
        step = 1
        while True:
            if x <= right:
                break
            step += 1
            left = right + 1
            right += a + ((step - 1) * d)

        print(step, x - left + 1)
