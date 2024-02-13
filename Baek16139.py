import sys

input = sys.stdin.readline

# input
string = input().strip()
q = int(input().strip())

# cnt[문자열 idx][문자 번호]
cnt = [[0] * 26]
char = [0] * 26
for idx in range(1, len(string)+1):
    char_idx = ord(string[idx-1]) - 97
    char[char_idx] += 1
    cnt.append(char[:])

"""
print("")
for _ in range(len(cnt)):
    print(_, cnt[_])
"""

for _ in range(q):
    key, l, r = input().strip().split()
    key_idx = ord(key)-97
    print(cnt[int(r)+1][key_idx] - cnt[int(l)][key_idx])
