import sys
from collections import deque

input = sys.stdin

# 입력단
n, m = map(int, input.readline().strip().split())
index = list(map(int, input.readline().strip().split()))

que = deque()

for i in range(n):
    que.append(i + 1)

qc = n  # 큐의 크기
ic = 0  # index에서 원소 위치
rotate = 0

while ic < m:
    mid = int(qc / 2)  # 큐의 중간 값

    if index[ic] == que[0]:
        que.popleft()
        qc -= 1
        ic += 1
    elif que.index(index[ic]) > mid:
        que.appendleft(que.pop())
        rotate += 1
    elif que.index(index[ic]) <= mid:
        que.append(que.popleft())
        rotate += 1

print(rotate)
