# 22/09/27
import sys

l, c = map(int, sys.stdin.readline().strip().split())
char = sorted(list(sys.stdin.readline().strip().split()))
vowel = ['a', 'e', 'i', 'o', 'u']
vst = [False] * c


def dfs(visited, curr):
    global l, c, ans, vowel

    if len(ans) == l:
        cnt_vowel = 0
        cnt_consonant = 0
        for j in range(l):
            if ans[j] in vowel:
                cnt_vowel += 1
            else:
                cnt_consonant += 1
        if cnt_vowel >= 1 and cnt_consonant >= 2:
            print(''.join(ans))
        return

    for i in range(curr, c):
        if not visited[i]:
            visited[i] = True
            ans.append(char[i])

            dfs(visited, i)
            visited[i] = False
            ans.pop()


if __name__ == '__main__':
    ans = []
    dfs(vst, 0)
