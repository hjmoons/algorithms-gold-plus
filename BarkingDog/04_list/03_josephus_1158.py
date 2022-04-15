import sys

input = sys.stdin.readline
n, k = map(int, input().strip().split())

circle = [i + 1 for i in range(n)]
result = []
index = 0       # 현재 인덱스

while circle:
    index += k - 1

    if index > len(circle) - 1:
        index %= len(circle)

    result.append(circle[index])
    del circle[index]

print("<" + str(result)[1:-1] + ">")

''' 시간초과
from collections import deque

circle = deque([i + 1 for i in range(n)])
result = []
index = 0

while circle:
    if index == k - 1:
        result.append(circle.popleft())
        index = 0
    else:
        circle.append(circle.popleft())
        index += 1
'''