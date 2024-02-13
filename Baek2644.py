# 22/09/07
import sys
sys.setrecursionlimit(10001)


def bfs(current_node,final,depth):
    print("%d visited"%(current_node))
    visited[current_node] = True
    if current_node == final:
        print("arrive to final")
        print("current depth = %d"%(depth))
        return depth
    for next in graph[current_node]:
        if not visited[next]:
            bfs(next,final,depth+1)


if __name__ == '__main__' :
    input = sys.stdin.readline
    n = int(input().strip())
    a,b = map(int,input().strip().split())
    num_edge = int(input().strip())
    graph = [[] for _ in range(n+1)]

    for _ in range(num_edge):
        x,y = map(int,input().strip().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False]*(n+1)
    print(graph)
    print(bfs(a,b,0))