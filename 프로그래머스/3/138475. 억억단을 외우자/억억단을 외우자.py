def solution(e, starts):
    dp = [0] * (e + 1)
    for i in range(1, int(e ** 0.5) + 1):
        dp[i * i] += 1
        for j in range(i * (i+1), e + 1, i):
            dp[j] += 2
    
    sorted_starts = sorted(starts)
    max_dict = dict()
    max_idx = 0
    for i in range(len(sorted_starts)):
        # 최대 등장 idx보다 현재 idx가 더 큰 경우, 갱신
        if sorted_starts[i] > max_idx:
            max_idx = dp[sorted_starts[i]:].index(max(dp[sorted_starts[i]:])) + sorted_starts[i]
            max_dict[sorted_starts[i]] = max_idx
        else:
            max_dict[sorted_starts[i]] = max_idx
            
    answer = []
    for i in range(len(starts)):
        answer.append(max_dict[starts[i]])
        
    return answer