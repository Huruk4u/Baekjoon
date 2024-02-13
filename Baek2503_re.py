import sys
from itertools import permutations

input = sys.stdin.readline

if __name__ == '__main__':
    # input
    n = int(input().strip())
    baseball = []
    for _ in range(n):
        baseball.append(list(map(int, input().strip().split())))

    # possible field
    possible = list(permutations([i for i in range(1, 10)], 3))

    # solve
    for number, strike, ball in baseball:
        number_tuple = tuple(map(int, str(number)))
        new_possible = []

        for possible_num in possible:
            strike_cnt = 0
            ball_cnt = 0
            for i in range(3):
                # 최소한 볼인가?
                if possible_num[i] in number_tuple:
                    # strike?
                    if possible_num[i] == number_tuple[i]:
                        strike_cnt += 1
                    else:
                        ball_cnt += 1

            if strike_cnt == strike and ball_cnt == ball:
                new_possible.append(possible_num)

        possible = new_possible

    print(len(possible))
