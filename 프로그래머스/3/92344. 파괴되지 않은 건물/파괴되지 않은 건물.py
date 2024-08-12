# 누적합?
def solution(board, skill):
    
    pSum = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    for i in range(len(skill)):
        type, r1, c1, r2, c2, degree = skill[i]
        if type == 1: degree *= -1
        
        pSum[r1][c1] += degree
        pSum[r2+1][c1] += -degree
        pSum[r1][c2+1] += -degree
        pSum[r2+1][c2+1] += degree
    
    for i in range(len(pSum)-1):
        for j in range(len(pSum[0])-1):
            pSum[i][j+1] += pSum[i][j]

    for j in range(len(pSum[0])-1):
        for i in range(len(pSum)-1):
            pSum[i+1][j] += pSum[i][j]
    
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += pSum[i][j]
            if board[i][j] > 0: answer += 1
    
    return answer