def solution(N, times):
    
    def enough(minute):
        cnt = 0
        for t in times:
            cnt += minute // t
            if cnt >= N:
                return True
        return False
    
    answer = 0
    left, right = 1, max(times) * N
    while left <= right:
        mid = (left + right) // 2
        if enough(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer