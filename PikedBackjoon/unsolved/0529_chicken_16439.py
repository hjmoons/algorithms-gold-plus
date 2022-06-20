import sys
from itertools import combinations

def solution(N, M, pre):
    answer = 0

    for a, b, c in combinations(range(M), 3):
        total = 0
        for i in range(N):
            total += max(pre[i][a], pre[i][b], pre[i][c])
        answer = max(answer, total)
    return answer


if __name__ == '__main__':
    input = sys.stdin.readline

    N, M = map(int, input().rstrip().split())
    pre = []
    for _ in range(N):
        pre.append(list(map(int, input().rstrip().split())))

    print(solution(N, M, pre))
