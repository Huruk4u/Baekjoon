def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    i, j = 0, 0
    while j < len(B):
        # 승점을 딸 수 있는 경우
        if A[i] < B[j]:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1
            
    return answer