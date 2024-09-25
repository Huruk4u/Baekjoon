import heapq


def solution(food_times, K):
    if sum(food_times) <= K:
        return -1
    
    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i + 1))

    cycle = 0
    total_time = 0
    length = len(food_times)
    while total_time + ((heap[0][0] - cycle) * len(heap)) <= K:
        curr = heapq.heappop(heap)[0]
        total_time += (curr - cycle) * length
        length -= 1
        cycle = curr

    rtn = sorted(heap, key=lambda x: x[1])
    return rtn[(K - total_time) % len(heap)][1]

    return -1