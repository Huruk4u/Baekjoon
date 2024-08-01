def solution(stones, k):
    answer = 0
    
    # pivot: 지나간 친구들의 수, pivot_list: 정렬된 돌의 숫자
    pivot_list = sorted(list(set(stones)))

    prev_stone, number_to_idx = dict(), dict()
    stones = [200001] + stones + [200001] # start + stones + end
    # [inf, 2, 4, 5, 3, 2, 1, 4, 2, 5, 1, inf]
    for i in range(1, len(stones) - 1):
        if i != 0: prev_stone[i] = i-1
        else: prev_stone[i] = 0
        
        if stones[i] not in number_to_idx: number_to_idx[stones[i]] = [i]
        else: number_to_idx[stones[i]].append(i)
        
    jump = dict()
    for i in range(len(stones)):
        jump[i] = 1
        
    for pivot in pivot_list:
        # if pivot = 1 -> idx = [5, 9]
        for idx in number_to_idx[pivot]:
            jump[prev_stone[idx]] += jump[idx]
            prev_stone[idx + jump[idx]] = prev_stone[idx]
            if jump[prev_stone[idx]] > k:
                return pivot
    
    return answer