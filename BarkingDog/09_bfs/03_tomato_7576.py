import sys
from collections import deque


def bfs(n, m, box, visited, x, y):
    tomatos = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append([x, y])
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

def solution(n, m, box):
    answer = 0
    visited = [[0] * m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if box[x][y] == 1:   # 노드가 1이면 그림 시작
                answer += bfs(n, m, box, visited, x, y)

    return answer


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().rstrip().split())
    box = [list(map(int, input().rstrip().split())) for _ in range(n)]

    p, ma = solution(n, m, box)
    print(p)
    print(ma)