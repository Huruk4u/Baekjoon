def solution(stones, k):
    answer = 0
    sorted_stones = []
    for i in range(len(stones)):
        sorted_stones.append((stones[i], i))
    sorted_stones.sort()
    
    prev = [i-1 for i in range(len(stones) + 2)]
    next = [i+1 for i in range(len(stones) + 2)]
    
    # O(N)
    for num, idx in sorted_stones:
        jump = next[idx] - prev[idx]
        if jump > k:
            answer = num
            break

        prev[next[idx]] = prev[idx]
        next[prev[idx]] = next[idx]
    
    return answer