import sys

a = int(sys.stdin.readline().strip())
words = []

for i in range(a):
     b = sys.stdin.readline().strip()
     words.append(b)

res = sorted(set(words), key=lambda x: (len(x),x))
for word in res:
    print(word)