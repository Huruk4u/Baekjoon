import sys
from collections import defaultdict

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    ipt = [input().strip() for _ in range(N)]
    char_weight = defaultdict(int)
    for string in ipt:
        x = len(string) - 1
        for s in string:
            char_weight[s] += 10**x
            x -= 1

    answer = 0
    num = 9
    char_priority = sorted(char_weight.values(), reverse=True)
    for c in char_priority:
        answer += c * num
        num -= 1

    print(answer)
