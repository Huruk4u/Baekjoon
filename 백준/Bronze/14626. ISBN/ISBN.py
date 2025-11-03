import sys
input = sys.stdin.readline


if __name__ == '__main__':
    isbn = input().strip()
    check_sign = int(isbn[-1])

    temp = 0
    unknown_number_weight = 0

    for number, weight in zip(isbn[:-1], [1, 3] * 6):
        if number == '*':
            unknown_number_weight = weight
            continue
        temp += int(number) * weight

    for unknown_number in range(10):
        rest = (temp + (unknown_number * unknown_number_weight) + check_sign) % 10
        if not rest:
            print(unknown_number)
            break