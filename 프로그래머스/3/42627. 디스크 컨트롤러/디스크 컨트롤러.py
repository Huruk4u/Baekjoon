import heapq
from collections import deque

def solution(jobs):
    
    N = len(jobs)
    # 요청 대기 중인 request
    heapq.heapify(jobs)
    heap = []
    # 이전 작업의 종료 시간
    prev_end, total = 0, 0
    while heap or jobs:
        # 수행 중인 작업이 없을 때
        if not heap:
            start, proc = heapq.heappop(jobs)
            prev_end = start
            heapq.heappush(heap, (proc, start))
        else:
            process, start = heapq.heappop(heap)
            ready_time = 0

            # 이전 작업의 종료 시간이 요청 시간보다 늦을 때
            if prev_end > start:
                ready_time = prev_end - start
            prev_end += process
            total += ready_time + process
            
            while True:
                if jobs and jobs[0][0] < prev_end:
                    start, proc = heapq.heappop(jobs)
                    heapq.heappush(heap, (proc, start))
                else:
                    break
                    
    return total // N