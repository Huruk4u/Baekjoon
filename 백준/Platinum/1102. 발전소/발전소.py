import sys

input = sys.stdin.readline

INF = sys.maxsize


def dfs(state, depth):
    # 켜진 발전소가 P개 이상이 된 경우
    if depth >= P:
        return 0

    if dp[state] != INF:
        return dp[state]

    for curr in range(N): # 발전소를 켜주는 노드
        # 만약 curr node가 0인 상태면 진행을 할 수 없다.
        if not state & (1 << curr): continue
        for next in range(N):  # 꺼져있는 발전소
            # 만약 next node 1인 상태면, 발전소를 킬 필요가 없다.
            if state & (1 << next): continue
            dp[state] = min(dp[state], cost[curr][next] + dfs(state | (1 << next), depth + 1))

    return dp[state]


if __name__ == '__main__':
    N = int(input().strip())
    cost = [list(map(int, input().strip().split())) for _ in range(N)]

    ipt = input().strip()
    P = int(input().strip())

    # bit masking 처음 state 설정
    dp = [INF] * (1 << N)
    state, depth = 0, 0
    for i in range(len(ipt)):
        if ipt[i] == "N": continue
        state = state | (1 << i)
        depth += 1

    rtn = dfs(state, depth)
    if rtn == INF: print(-1)
    else: print(rtn)