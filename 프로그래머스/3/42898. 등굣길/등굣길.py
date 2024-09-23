def solution(M, N, puddles):

    MOD = 1000000007
    
    matrix = [[0] * M for _ in range(N)]
    for x, y in puddles:
        matrix[y-1][x-1] = 1
        
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(M):
            if matrix[i][j]: continue
            if i == 0 and j == 0: continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[N-1][M-1] % MOD