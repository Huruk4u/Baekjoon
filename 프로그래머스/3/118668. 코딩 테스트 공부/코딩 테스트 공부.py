import sys
INF = sys.maxsize


def solution(sa, sc, problems):
    ea, ec = sa, sc
    for algo, cod, a, b, c in problems:
        ea = max(ea, algo)
        ec = max(ec, cod)

    if sa >= ea and sc >= ec:
        return 0
        
    # dp[algo][cod] = [algo][cod]에 도달할 수 있는 최소 cost
    dp = [[INF] * (ec+1) for _ in range(ea+1)]
    dp[sa][sc] = 0
    
    for algo in range(sa, ea+1):
        for cod in range(sc, ec+1):
            next_algo = algo + 1 if algo + 1 < ea + 1 else ea
            dp[next_algo][cod] = min(dp[next_algo][cod], dp[algo][cod] + 1)
            
            next_cod = cod + 1 if cod + 1 < ec + 1 else ec
            dp[algo][next_cod] = min(dp[algo][next_cod], dp[algo][cod] + 1)
            
            for rq_algo, rq_cod, dt_algo, dt_cod, cost in problems:
                if algo < rq_algo or cod < rq_cod:
                    continue
                next_algo = algo + dt_algo if algo + dt_algo < ea + 1 else ea
                next_cod = cod + dt_cod if cod + dt_cod < ec + 1 else ec
                dp[next_algo][next_cod] = min(dp[next_algo][next_cod], dp[algo][cod] + cost)
    
    return dp[ea][ec]