import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10000001)


def max_route(curr):
    global diameter
    print("curr %d" % curr)
    # leaf node
    if not tree[curr]:
        return 0

    route = []
    for i in range(len(tree[curr])):
        new_route = weight[curr][i] + max_route(tree[curr][i])
        heapq.heappush(route, (-new_route, new_route))

    print("\n============================ curr = %d ============================" % curr)
    route1 = heapq.heappop(route)[1]
    diameter = max(route1, diameter)
    if route:
        route2 = heapq.heappop(route)[1]
        diameter = max(route1 + route2, diameter)
    print("diameter = %d" % diameter)
    return route1


if __name__ == '__main__':
    n = int(input().strip())

    tree = [[] for _ in range(n+1)]
    weight = [[] for _ in range(n+1)]
    for _ in range(n-1):
        p, c, w = map(int, input().strip().split())
        tree[p].append(c)
        weight[p].append(w)

    print(tree)
    print(weight)

    diameter = 0
    max_route(1)

    print(diameter)
