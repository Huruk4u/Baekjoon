import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000001)


def in_range(x, y):
    if (0 <= y < H) and (0 <= x < W):
        return True
    else:
        return False

def find_way(x, y, d, passed_clean_q: list):
    # print(f'현재 노드: {x}, {y}')
    if not in_range(x, y):
        return 0
    elif passed_clean_q and (x, y, d) == passed_clean_q[0]:
        return 0

    if is_dirty[y][x]:
        is_dirty[y][x] = False          # 청소
        rtn = len(passed_clean_q) + 1   # 여태 온 경로는 의미가 있는 경로로 판단
        # print(rtn, passed_clean_q)
        passed_clean_q.clear()          # 클린 큐 초기화
        nd = (d + rule_a[y][x]) % 4     # ruleA 적용하여 회전
    else:
        rtn = 0                         # 여기까지 온 경로는 아직 의미가 없는 경로임
        nd = (d + rule_b[y][x]) % 4     # ruleB 적용하여 회전
        passed_clean_q.append((x, y, d))    # 현재 노드를 다시 청소할 필요 없는 노드 목록에 추가

    nx, ny = x + dxdy[nd][0], y + dxdy[nd][1]           # 다음으로 갈 노드 결정
    return rtn + find_way(nx, ny, nd, passed_clean_q)   # 다음 탐색 시작

if __name__ == '__main__':
    # input
    H, W = map(int, input().strip().split())
    sy, sx, sd = map(int, input().strip().split())
    rule_a = [list(map(int, input().strip())) for _ in range(H)]
    rule_b = [list(map(int, input().strip())) for _ in range(H)]
    is_dirty = [[True] * W for _ in range(H)]
    dxdy = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # print(find_way(sx, sy, sd, []))
    passed_clean_q = []
    x, y, d = sx, sy, sd
    ans = 0
    while True:
        # print(f'현재 노드: {x}, {y}')
        if not in_range(x, y):
            break
        elif passed_clean_q and (x, y, d) == passed_clean_q[0]:
            break

        if is_dirty[y][x]:
            is_dirty[y][x] = False  # 청소
            ans += len(passed_clean_q) + 1  # 여태 온 경로는 의미가 있는 경로로 판단
            # print(passed_clean_q)
            passed_clean_q.clear()  # 클린 큐 초기화
            nd = (d + rule_a[y][x]) % 4  # ruleA 적용하여 회전
        else:
            # 여기까지 온 경로는 아직 의미가 없는 경로임
            nd = (d + rule_b[y][x]) % 4  # ruleB 적용하여 회전
            passed_clean_q.append((x, y, d))  # 현재 노드를 다시 청소할 필요 없는 노드 목록에 추가

        nx, ny = x + dxdy[nd][0], y + dxdy[nd][1]  # 다음으로 갈 노드 결정
        x, y, d = nx, ny, nd

    print(ans)
