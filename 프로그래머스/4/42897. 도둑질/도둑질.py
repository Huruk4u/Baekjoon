def solution(money):
    N = len(money) + 1
    
    pick1_money = money[:]
    pick1_money[-1], pick1_money[1] = 0, 0
    pick1 = [[0, 0] for _ in range(N)]
    for i in range(1, N):
        pick1[i][0] = max(pick1[i-1][0], pick1[i-1][1])
        pick1[i][1] = pick1[i-1][0] + pick1_money[i-1]

    pickN_money = money[:]
    pickN_money[0], pickN_money[-2] = 0, 0
    pickN = [[0, 0] for _ in range(N)]
    for i in range(1, N):
        pickN[i][0] = max(pickN[i-1][0], pickN[i-1][1])
        pickN[i][1] = pickN[i-1][0] + pickN_money[i-1]
    
    answer = max(max(pick1[N-1]), max(pickN[N-1]))
    return answer