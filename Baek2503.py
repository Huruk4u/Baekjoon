import sys

input = sys.stdin.readline


def check_strike(n_strike, possible_s, str_num):
    # 1 strike
    if n_strike == 1:
        if possible_s[0] == str_num[0] or possible_s[1] == str_num[1] or possible_s[2] == str_num[2]:
            return True
        else:
            return False
    # 2 strike
    else:
        if (possible_s[0] == str_num[0] and possible_s[1] == str_num[1]) or (possible_s[1] == str_num[1] and possible_s[2] == str_num[2]) or (possible_s[0] == str_num[0] and possible_s[2] == str_num[2]):
            return True
        else:
            return False


def check_ball(n_ball, n_strike, possible_set, set_num):
    # 1 ball
    if n_ball == 1:
        if len(set.intersection(possible_set, set_num)) == 1:
            return True
        else:
            return False
    # 2 ball
    elif n_ball == 2 or (n_ball == 1 and n_strike == 1):
        if len(set.intersection(possible_set, set_num)) == 2:
            return True
        else:
            return False
    # 3 ball
    elif n_ball == 3 or (n_ball == 1 and n_strike == 2):
        if len(set.intersection(possible_set, set_num)) == 3:
            return True
        else:
            return False


if __name__ == '__main__':
    n = int(input().strip())
    baseball = []
    for _ in range(n):
        baseball.append(list(map(int, input().strip().split())))

    # 1~9까지 겹치는 숫자가 없는 조합, 1000
    possible = []
    for num in range(123, 1000):
        s = str(num)
        if s[0] != s[1] and s[1] != s[2] and s[0] != s[2] and '0' not in s:
            possible.append(num)

    # solve
    for num, strike, ball in baseball:
        print("%d %d %d" % (num, strike, ball))
        new_possible = []
        # 1000
        for pos in possible:
            if strike and ball:
                if check_ball(ball, strike, set(str(pos)), set(str(num))) and check_strike(strike, str(pos), str(num)):
                    new_possible.append(pos)
            elif strike:
                if check_strike(strike, str(pos), str(num)):
                    new_possible.append(pos)
            elif ball:
                if check_ball(ball, strike, set(str(pos)), set(str(num))):
                    new_possible.append(pos)
            else:
                if not set.intersection(set(str(pos)), set(str(num))):
                    new_possible.append(pos)

        print(new_possible)
        possible = new_possible
        print(possible)


    print(possible)
