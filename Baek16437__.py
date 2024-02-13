import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000001)


def solution(curr, sheep):
    is_wolf, n_obj = state[curr]
    # escape
    if curr == 1:
        return sheep

    if not is_wolf:
        sheep += n_obj
        state[curr][1] -= n_obj
    else:
        if sheep < n_obj:
            sheep = 0
            state[curr][1] -= sheep
        else:
            sheep -= n_obj
            state[curr][1] = 0

    return solution(parent[curr], sheep)


if __name__ == '__main__':
    n = int(input().strip())

    # is_leaf
    is_leaf = [True] * (n+1)

    # parent, state
    parent = [0] * (n+1)
    state = [[] for _ in range(n+1)]
    state[1] = [0, 0]

    for i in range(2, n+1):
        t, a, p = input().strip().split()
        # edge : child -> parent
        parent[i] = int(p)
        is_leaf[int(p)] = False
        if t == 'S':
            state[i] = [0, int(a)]
        else:
            state[i] = [1, int(a)]

    ans = 0
    for i in range(2, n+1):
        if is_leaf[i]:
            ans += solution(i, 0)

    print(ans)
