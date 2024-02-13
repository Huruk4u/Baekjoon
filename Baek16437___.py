import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000001)


def postorder(curr, sheep):
    for c in child[curr]:
        sheep += postorder(c, 0)

    is_wolf, n_obj = state[curr]

    if is_wolf:
        if sheep >= n_obj:
            sheep -= n_obj
            state[curr][1] = 0
        else:
            sheep = 0
            state[curr][1] -= sheep
    else:
        sheep += n_obj

    return sheep


if __name__ == '__main__':
    n = int(input().strip())

    child = [[] for _ in range(n+1)]
    state = [[] for _ in range(n+1)]
    state[1] = [0, 0]

    for i in range(2, n+1):
        t, a, p = input().strip().split()
        if t == 'S':
            child[int(p)].append(i)
            state[i] = [0, int(a)]
        else:
            child[int(p)].append(i)
            state[i] = [1, int(a)]

    print(postorder(1, 0))
