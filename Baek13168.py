import sys
input = sys.stdin.readline
INF = sys.maxsize


def floyd_warshall():
    for k in range(N):
        for u in range(N):
            for v in range(N):
                new_cost_1 = cost_1[u][k] + cost_1[k][v]
                new_cost_2 = cost_2[u][k] + cost_2[k][v]
                if new_cost_1 < cost_1[u][v]:
                    cost_1[u][v] = new_cost_1
                if new_cost_2 < cost_2[u][v]:
                    cost_2[u][v] = new_cost_2

    return


if __name__ == '__main__':
    N, R = map(int, input().strip().split())

    ipt = set(input().strip().split())
    city = dict()
    i = 0
    for c in ipt:
        city[c] = i
        i += 1

    M = int(input().strip())
    path = list(input().strip().split())

    K = int(input().strip())
    cost_1 = [[INF] * N for _ in range(N)]  # 내일로 티켓 선택X
    cost_2 = [[INF] * N for _ in range(N)]  # 내일로 티켓 선택
    for _ in range(K):
        t, s, e, c = map(str, input().strip().split())
        if cost_1[city[s]][city[e]] < int(c):
            continue
        cost_1[city[s]][city[e]] = int(c)
        cost_1[city[e]][city[s]] = int(c)

        if t == "S-Train" or t == "V-Train":
            if cost_2[city[s]][city[e]] < float(int(c) / 2):
                continue
            cost_2[city[s]][city[e]] = float(int(c) / 2)
            cost_2[city[e]][city[s]] = float(int(c) / 2)
        elif t == "ITX-Saemaeul" or t == "ITX-Cheongchun" or t == "Mugunghwa":
            cost_2[city[s]][city[e]] = 0
            cost_2[city[e]][city[s]] = 0
        else:
            if cost_2[city[s]][city[e]] < float(c):
                continue
            cost_2[city[s]][city[e]] = float(c)
            cost_2[city[e]][city[s]] = float(c)

    floyd_warshall()

    print(city)

    totalCost_1 = 0
    totalCost_2 = R
    for i in range(1, M):
        start = path[i-1]
        end = path[i]
        print("---------------------------------------")
        print("%s =======> %s" % (start, end))
        print("totalCost += cost[%d][%d]" % (city[start], city[end]))
        totalCost_1 += cost_1[city[start]][city[end]]
        print(cost_1[city[start]][city[end]], cost_2[city[start]][city[end]])
        totalCost_2 += cost_2[city[start]][city[end]]
        print()

    print(totalCost_1, totalCost_2)
    if totalCost_1 > totalCost_2:
        print("Yes")
    else:
        print("No")
