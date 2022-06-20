import sys
from collections import deque

# 입력된 도화지에서 색칠된 모든 x, y 좌표 탐색
def bfs(n, m, canvas, x, y):
    area = 1    # 그림 넓이, 1인 노드를 방문했으므로 너비 1로 시작
    # 상하좌우에 그림이 있는지 확인하는 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append([x, y])
    canvas[x][y] = 0 # 시작점 방문처리

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # x, y좌표의 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and canvas[nx][ny] == 1:
                area += 1   # 그림 넓이 증가
                canvas[nx][ny] = 0  # 방문했으면 0으로 변경
                queue.append([nx, ny])  # 그림의 다음부분 탐색을 위해 큐에 추가

    return area


def solution(n, m, canvas):
    picture = 0 # 그림의 개수
    areas = []  # 그림의 넓이 배열

    for x in range(n):
        for y in range(m):
            if canvas[x][y] == 1:   # 노드가 1이면 그림 시작
                picture += 1
                areas.append(bfs(n, m, canvas, x, y))

    max_area = max(areas)
    return picture, max_area


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().rstrip().split())
    canvas = [list(map(int, input().rstrip().split())) for _ in range(n)]
    
    p, ma = solution(n, m, canvas)
    print(p)
    print(ma)
