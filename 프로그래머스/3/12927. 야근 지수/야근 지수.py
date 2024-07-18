import heapq

def solution(N, works):
    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap, -work)
    
    for _ in range(N):
        max_work = -heapq.heappop(heap)
        if max_work - 1 <= 0:
            max_work = 0
        else:
            max_work -= 1
        heapq.heappush(heap, -max_work)
    
    while heap:
        temp = -heapq.heappop(heap)
        answer += temp**2
        
    return answer