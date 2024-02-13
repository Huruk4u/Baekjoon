import sys

input = sys.stdin.readline


def solve(length):
    global k
    # return
    if length == 1:
        return

    solve(length - 1)

    # get previent dp
    prev_dp = dp.get(length - 1)
    curr_dp = set()

    s = int(str(k) * length)
    curr_dp.add(s)

    print("======================\n length = %d" % length)
    for prev_n in prev_dp:
        curr_dp.add(abs(prev_n - k))
        curr_dp.add(prev_n + k)
        curr_dp.add(prev_n * k)
        if prev_n:
            curr_dp.add(prev_n // k)
    print("curr_dp", curr_dp)

    dp[length] = curr_dp


if __name__ == '__main__':
    k = int(input().strip())
    n = int(input().strip())

    dp = dict()
    dp[0] = {0}
    dp[1] = {k}

    solve(8)

    for _ in range(n):
        ipt = int(input().strip())
        flag = False

        for i in range(1, 9):
            if ipt in dp[i]:
                print(i)
                flag = True
                break
        if not flag:
            print("NO")
