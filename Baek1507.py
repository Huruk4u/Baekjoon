import sys
input = sys.stdin.readline
INF = sys.maxsize


def floyd_warshall():
    for k in range(N):
        for u in range(N):
            for v in range(N):
                if u == k or k == v or u == v:
                    continue
                new_dist = dist[u][k] + dist[k][v]
                if dist[u][v] == new_dist:
                    edge.add((u, v))
                elif dist[u][v] > new_dist:
                    return False
    return True


if __name__ == '__main__':
    N = int(input().strip())
    dist = []
    for _ in range(N):
        dist.append(list(map(int, input().strip().split())))

    edge = set()
    valid = floyd_warshall()

    if valid:
        for u, v in edge:
            dist[u][v] = 0
        rtn = 0
        for _ in range(N):
            rtn += sum(dist[_])
        print(rtn // 2)
    else:
        print(-1)
