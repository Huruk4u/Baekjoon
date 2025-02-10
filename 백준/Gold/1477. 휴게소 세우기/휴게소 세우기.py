import sys
input = sys.stdin.readline


"""
    휴게소를 x간격 이내로 설치하는 것이 가능한 경우 return True else False
"""
def is_good(x):
    cnt = 0
    for i in range(N+1):
        if rest[i+1] - rest[i] > x:
            dist = rest[i+1] - rest[i]
            if dist % x == 0:
                cnt += (dist // x) - 1
            else:
                cnt += dist // x

    if cnt > M:
        return False
    else:
        return True

if __name__ == '__main__':
    """
        N : 현재 휴게소의 갯수
        M : 더 지으려고 하는 휴게소의 갯수
        L : 고속도로의 길이
    """
    N, M, L = map(int, input().strip().split())
    rest = list(map(int, input().strip().split()))
    rest = [0] + sorted(rest) + [L]

    """
        처음 그리디로 시도했는데 실패. 
        반례 (100, 400, 500) 2개의 휴게소를 설치해야 하는 경우. 그리디는 100과 400의 중간지점에 설치함
        이분탐색으로 진행함.
    """
    left, right = 1, L
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        if is_good(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)