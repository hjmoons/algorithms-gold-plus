import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().strip().split())

'''
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

circle = [i + 1 for i in range(n)]
result = []
index = 0

while circle:
    if index == k - 1:
        del circle[index]



print("<" + str(result)[1:-1] + ">")