import sys
input = sys.stdin.readline


def dist(loc_u, loc_v):
    ux, uy, uz = loc_u
    vx, vy, vz = loc_v
    return min(abs(ux - vx), abs(uy - vy), abs(uz - vz))


def find(curr):
    if parent[curr] == curr:
        return curr
    parent[curr] = find(parent[curr])
    return parent[curr]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return False
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
    return True


if __name__ == '__main__':
    N = int(input().strip())
    loc = [tuple(map(int, input().strip().split())) for _ in range(N)]
    planet = dict()
    for i in range(N):
        planet[loc[i]] = i

    loc_x = loc[:]
    loc_y = loc[:]
    loc_z = loc[:]

    loc_x.sort(key=lambda x: x[0])
    loc_y.sort(key=lambda x: x[1])
    loc_z.sort(key=lambda x: x[2])

    edge = []
    for i in range(1, N):
        edge.append((planet[loc_x[i-1]], planet[loc_x[i]], dist(loc_x[i-1], loc_x[i])))
        edge.append((planet[loc_y[i-1]], planet[loc_y[i]], dist(loc_y[i-1], loc_y[i])))
        edge.append((planet[loc_z[i-1]], planet[loc_z[i]], dist(loc_z[i-1], loc_z[i])))
    edge.sort(key=lambda x: x[2])

    parent = [i for i in range(N)]
    totalCost = 0
    for u, v, cost in edge:
        if union(u, v):
            totalCost += cost

    print(totalCost)
