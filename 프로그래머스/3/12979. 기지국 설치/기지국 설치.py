def solution(N, stations, w):
    
    # 송신탑의 커버 범위
    point = []
    for i in range(len(stations)):
        left, right = stations[i] - w, stations[i] + w
        left  = stations[i] - w if left > 1 else 1
        right = stations[i] + w if right < N+1 else N
        point.append((left, right))
    
    start, apart = 1, []
    for left, right in point:
        if left > start:
            apart.append((start, left - 1))
        start = right + 1
    if start <= N:
        apart.append((start, N))
    
    answer = 0
    for left, right in apart:
        apart_len = right - left + 1
        cover_len = (w * 2) + 1
        if apart_len % cover_len == 0:
            answer += apart_len // cover_len
        else:
            answer += (apart_len // cover_len) + 1
        
    
    return answer