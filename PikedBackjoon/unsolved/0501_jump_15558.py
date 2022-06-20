# 다시 풀어볼 문제

import sys

input = sys.stdin.readline

N, k = map(int, input().rstrip().split())
left = list(map(int, input().rstrip()))
right = list(map(int, input().rstrip()))

i = 0
cur = 0
while i < N:
    print(i)
    if left[i+1] == 1:     # 왼쪽줄
        i += 1
    elif right[i+k] == 1:
        i += k
        temp = left
        left = right
        right = left
    else:
        i -= 1


'''
from collections import deque

def solve():
    N, K = map(int, input().split())
    A = [input(), input()]

    DIRS = ((0, 1), (0, -1), (1, K))

    visit = [[-1] * N for _ in range(2)]
    visit[0][0] = 0

    queue = deque()
    queue.append([0, 0])

    while queue:
        r, c = queue.popleft()

        for dr, dc in DIRS:
            nr, nc = (r + dr) % 2, c + dc

            # 유효성 검사
            if nc < 0: continue

            # 도착
            if nc >= N: return 1

            # 방문 칸 넘기기
            if visit[nr][nc] != -1: continue
            visit[nr][nc] = visit[r][c] + 1

            # 없어진 칸 넘기기
            if visit[nr][nc] > nc: continue

            # 위험 칸 넘기기
            if A[nr][nc] == '0': continue

            queue.append([nr, nc])

    return 0


if __name__ == "__main__":
    print(solve())
'''