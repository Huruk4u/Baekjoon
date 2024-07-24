def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)]
    
    for n in range(1, 9):
        # 5, 55, 555, 5555...
        dp[n].add(int(str(N) * n))
        for i in range(n):
            for opr1 in dp[i]:
                for opr2 in dp[n-i]:
                    dp[n].add(opr1 + opr2)
                    dp[n].add(opr1 - opr2)
                    dp[n].add(opr1 * opr2)
                    if opr1 != 0 and opr2 != 0: dp[n].add(opr1 // opr2)
        if number in dp[n]:
            return n
        
    return -1