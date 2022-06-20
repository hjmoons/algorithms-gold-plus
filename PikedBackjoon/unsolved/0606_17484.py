import sys


def dfs(depth, h, dir):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += h[n] - set(visited)
    return visited

def solution(N, M, h):
    answer = 0

    i, j = 0, 0

    while True:
        i
    return answer


if __name__ == '__main__':
    input = sys.stdin.readline

    N, M = map(int, input().rstrip().split())
    h = [list(map(int, input().rstrip().split())) for _ in range(N)]

    print(*solution(N, M, h))
