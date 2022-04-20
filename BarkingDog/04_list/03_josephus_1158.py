import sys

input = sys.stdin.readline
n, k = map(int, input().strip().split())

circle = [i + 1 for i in range(n)]
result = []
index = 0       # 현재 인덱스

while circle:       # 원에 수가 존재하지 않을 때까지
    index += k - 1  # 시작 index에서 k-1을 더한 위치가 제거할 수가 있는 위치

    if index > len(circle) - 1:     # index가 현재 원에 있는 수의 개수를 넘어갈 경우
        index %= len(circle)        # 원의 맨 처음 index로 다시 돌아감

    result.append(circle[index])    # 해당 index를 결과에 추가
    del circle[index]               # del 연산을 통해 수를 제거하고 뒤에 있는 수들을 앞으로 당김 O(n)

print("<" + str(result)[1:-1] + ">")

# 연결 리스트 구현해서 풀어보기

''' 시간초과
from collections import deque

circle = deque([i + 1 for i in range(n)])
result = []
index = 0
circle.rotate(1) -> 시간복잡도 확인해보기

while circle:
    if index == k - 1:
        result.append(circle.popleft())
        index = 0
    else:
        circle.append(circle.popleft())
        index += 1
'''