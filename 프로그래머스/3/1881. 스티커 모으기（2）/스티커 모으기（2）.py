import sys, copy


def solution(sticker):
    N = len(sticker)
    
    if N == 1:
        return sticker[0]
    else:  
        dp1 = sticker[:-1]
        for i in range(N-1):
            if i == 0: 
                continue
            elif i == 1:
                dp1[i] = max(dp1[i-1], dp1[i])
            else:
                dp1[i] = max(dp1[i-2] + dp1[i], dp1[i-1])

        dp2 = sticker[1:]
        for i in range(N-1):
            if i == 0: 
                continue
            elif i == 1:
                dp2[i] = max(dp2[i], dp2[i-1])
            else:
                dp2[i] = max(dp2[i-2] + dp2[i], dp2[i-1])

        return max(dp1[-1], dp2[-1])