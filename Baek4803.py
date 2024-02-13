import sys

input = sys.stdin.readline


def preorder(past, curr):
    global flag
    print("노드 이동 %d -> %d" % (past, curr))
    visited[curr] = True
    for next_node in graph[curr]:
        print("next -> %d" % next_node)
        # 왔던 길인 경우
        if next_node == past:
            print("%d는 지나온 길 입니다." % next_node)
            continue
        if visited[next_node]:
            print("%d는 이미 방문한 노드입니다." % next_node)
            flag = False
            continue
        preorder(curr, next_node)
    return


if __name__ == '__main__':
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

        # 500
        for i in range(1, n+1):
            flag = True
            if not visited[i]:
                print("=========================== %d ===========================" % i)
                preorder(0, i)
                if flag:
                    tree += 1

        print(tree)
