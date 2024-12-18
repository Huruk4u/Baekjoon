import sys
from collections import defaultdict
input = sys.stdin.readline


def kind_and_amount(state):
    kind, amount = 0, 0
    for key in state.keys():
        if state[key]:
            kind += 1
            amount += state[key]
    return kind, amount

if __name__ == '__main__':
    N = int(input().strip())
    S = list(map(int, input().strip().split()))

    left, right = 0, 0
    state = defaultdict(int)
    state[S[0]] = 1
    answer = 0
    while right < N:
        kind, amount = kind_and_amount(state)
        # print("\n[%d, %d] kind, amount = %d, %d" % (left, right, kind, amount))
        if kind <= 2:
            answer = max(answer, amount)

        if left == right or kind <= 2:
            right += 1
            if right < N:
                state[S[right]] += 1
        else:
            state[S[left]] -= 1
            left += 1

    print(answer)
    