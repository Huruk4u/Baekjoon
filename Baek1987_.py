# 22/09/28
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(curr_x, curr_y, visited, depth):
    global dx, dy, ans

    visited[curr_y][curr_x] = True
    alphabet[ord(board[curr_y][curr_x]) - ord('A')] = True
    depth += 1
    for i in range(4):
        next_x = curr_x + dx[i]
        next_y = curr_y + dy[i]
        if (0 <= next_x < x) and (0 <= next_y < y):
            if not visited[next_y][next_x] and not alphabet[ord(board[next_y][next_x]) - ord('A')]:
                dfs(next_x, next_y, visited, depth)

                visited[next_y][next_x] = False
                alphabet[ord(board[next_y][next_x]) - ord('A')] = False

    ans = max(ans, depth)
    return


if __name__ == '__main__':
    y, x = map(int, sys.stdin.readline().strip().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(y)]
    vst = [[False] * x for _ in range(y)]
    alphabet = [False] * ((ord('Z') - ord('A')) + 1)

    ans = 0

    dfs(0, 0, vst, 0)
    print(ans)
