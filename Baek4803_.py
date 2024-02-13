import sys

input = sys.stdin.readline
sys.setrecursionlimit(100001)


def preorder(past, curr):
    global flag
    visited[curr] = True
    for next_node in graph[curr]:
        if next_node == past:
            continue
        if visited[next_node]:
            flag = False
            continue
        preorder(curr, next_node)
    return


if __name__ == '__main__':
    case = 1
    while True:
        n, m = map(int, input().strip().split())
        if n == m == 0:
            break

        # graph
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b = map(int, input().strip().split())
            graph[a].append(b)
            graph[b].append(a)

        # visited, number of tree
        visited = [False] * (n+1)
        tree = 0

        for i in range(1, n+1):
            flag = True
            if not visited[i]:
                preorder(0, i)
                if flag:
                    tree += 1

        if tree >= 2:
            print("Case %d: A forest of %d trees." % (case, tree))
        elif tree == 1:
            print("Case %d: There is one tree." % case)
        else:
            print("Case %d: No trees." % case)

        case += 1
