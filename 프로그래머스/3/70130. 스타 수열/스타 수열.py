import heapq

def solution(A):
    
    def count_star(x):
        temp = -1
        rtn = 0
        for i in range(N):
            # 아무것도 집지 않은 상태면
            if temp == -1:
                temp = A[i]
            # 뭐라도 집고 있는 상태면
            else:
                if temp == x and A[i] != x:
                    rtn += 1
                    temp = -1
                if temp != x and A[i] == x:
                    rtn += 1
                    temp = -1
        return rtn
    
    N = len(A)
    apr = [0 for _ in range(N)]
    for i in range(N):
        apr[A[i]] += 1

    # 빈도 수가 높은 수부터 교집합의 수로 정의
    heap = []   # heap[0] : (i가 등장한 빈도 수, i)
    for i in range(N):
        if apr[i]: heapq.heappush(heap, (-apr[i], i))
    
    answer = 0
    while heap:
        # x : 교집합 수
        appear, x = heapq.heappop(heap)
        if -appear <= answer: # 만약 x의 등장 빈도 수가 answer보다 같거나 작다면, 더이상 탐색할 이유 X
            continue
    
        answer = max(answer, count_star(x))
    
    return answer * 2