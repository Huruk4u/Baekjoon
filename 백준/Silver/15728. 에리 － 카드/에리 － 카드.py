import sys, heapq
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().strip().split())

    share = list(map(int, input().strip().split()))
    team = list(map(int, input().strip().split()))

    scores = []
    for share_card in share:
        for team_card in team:
            heapq.heappush(scores, (-(share_card * team_card), share_card, team_card))

    banned = set()
    while len(banned) < K:
        score, sc, tc = heapq.heappop(scores)
        if tc not in banned:
            banned.add(tc)

    answer = 0
    while True:
        answer, sc, tc = heapq.heappop(scores)
        if tc not in banned:
            break
    print(-answer)

