import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

start = 1
end = k
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, n + 1):
        count += min(int(mid / i), n)
    if count < k:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)